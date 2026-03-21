import numpy as np
import json
import math

# 这个函数用于处理numpy类型
def default_dump(obj):
    if isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj

#创建包含所有向量的类
class CoordinateSystem:
    def __init__(self,axes:list[list[float]],vectors:list[list[float]]=None):
        """初始化坐标系"""
        self.axes = np.array(axes) #原始坐标轴向量列表
        self.vectors = np.array(vectors) if vectors is not None else np.array([])#三元运算符
        self.dimension = len(self.axes[0]) #维度的判断利用的是基向量的长度，即基向量中的参数个数
        self.validate_axes() #判断是否是线性相关，如果是则不能成为基底

    def validate_axes(self):
        '''检查维度是否一致'''
        if len(self.axes) != self.dimension:
            raise ValueError(f"坐标轴数量 ({len(self.axes)}) 应等于维度 ({self.dimension})")
            #raise 是 Python 的关键字，用于手动引发（抛出）异常。当程序遇到某种错误情况，
            #而这种错误不是由 Python 运行时自动检测到的，而是由程序员在代码中明确判断出的，就需要使用 raise 来引发异常。

        # 检查坐标轴是否线性无关
        if np.linalg.matrix_rank(self.axes) < self.dimension:
            raise ValueError("坐标轴向量线性相关，不能构成有效坐标系")
        #np.linalg.matrix_rank 是 NumPy 线性代数库 (linalg) 中的一个函数，用于计算矩阵的秩。
        #矩阵的秩（Rank）是线性代数中的一个重要概念，表示：矩阵中线性无关的行向量的最大数量或者线性无关的列向量的最大数量也表示矩阵所包含的"真实信息量"

    def change_axis(self,obj_axis:list[list[float]])->list[list[float]]:
        '''将当前坐标系的向量转移到目标坐标系'''
        obj_axis = np.array(obj_axis)
        # 验证目标坐标系
        if obj_axis.shape[0] != self.dimension or obj_axis.shape[1] != self.dimension:
            raise ValueError(f"目标坐标系维度不匹配，应为 {self.dimension}x{self.dimension}")
        # 检查目标坐标系是否有效
        if np.linalg.matrix_rank(obj_axis) < self.dimension:
            raise ValueError("目标坐标系坐标轴线性相关，不能构成有效坐标系")
        # 计算变换矩阵的逆
        inv_obj_axis = np.linalg.inv(obj_axis)
        # 转换所有向量
        transformed_vectors = []
        for v in self.vectors:
            v_prime = np.dot(inv_obj_axis, v)
            transformed_vectors.append(v_prime.tolist())
        # 更新当前坐标系为新坐标系
        self.axes = obj_axis
        self.vectors = np.array(transformed_vectors)
        return transformed_vectors

    def axis_projection(self,vectors:list[list[float]] = None) -> list[list[float]]:
        '''计算向量在个坐标轴上的投影'''
        if vectors is None:
            vectors = self.vectors
        projections = []
        for v in vectors:
            proj = []
            for axis in self.axes:
                # 计算投影：v · axis
                proj.append(np.dot(v,axis))
            projections.append(proj)
        return projections

    def axis_angle(self, vectors:list[list[float]] = None) -> list[list[float]]:
        '''计算向量与目标坐标系各轴的夹角（弧度）'''
        if vectors is None:
            vectors = self.vectors
        angles = []
        for v in vectors:
            angle = []
            for axis in self.axes:
                dot_product = np.dot(v,axis)
                v_norm = np.linalg.norm(v)
                axis_norm = np.linalg.norm(axis)#np.linalg.norm 是 NumPy 线性代数模块中的一个函数，用于计算向量或矩阵的范数（Norm）。
                                                #范数是对向量或矩阵的度量，结果为标量值。简答来说就是模
                if v_norm == 0 or axis_norm == 0:
                    angle.append(0.0)
                else:
                    cos_theta = dot_product/(v_norm*axis_norm)
                    angle.append(math.acos(cos_theta)) #math.acos()是反余弦函数
                angles.append(angle)
        return angles

    def area(self,obj_axis:list[list[float]] = None) -> float:
        """计算坐标系的面积缩放因子（行列式的绝对值）"""
        if obj_axis is None:
            axis_matrix = self.axes
        else:
            axis_matrix = np.array(obj_axis)
        # 检查维度
        if axis_matrix.shape[0] != self.dimension or axis_matrix.shape[1] != self.dimension:
            raise ValueError(f"坐标系维度不匹配，应为 {self.dimension}x{self.dimension}")
        # 计算行列式
        det = np.linalg.det(axis_matrix)#np.linalg.det() 是 NumPy 线性代数模块 (linalg) 中的一个函数，用于计算方阵的行列式
        return abs(det)


#任务处理函数
def processing_data(task_group:dict[str,any])->dict[str,any]:#这个是Python中的类型提示(Type Hint)用于指定函数的参数类型和返回类型,Any表示字典的值可以是任何类型
    """
    处理一个任务组
    :param task_group: 任务组数据
    :return: 处理结果
    """
    # 创建坐标系
    cs = CoordinateSystem(axes=task_group["ori_axis"],vectors=task_group["vectors"])
    # 处理每个任务\
    results = {}
    for i,task in enumerate(task_group["tasks"]):
        task_type = task["type"]
        if task_type == "change_axis" :
            obj_axis = task["obj_axis"]
            result = cs.change_axis(obj_axis)
            results[f"task_{i+1}_{task_type}"] = result
        elif task_type == "axis_projection":
            result = cs.axis_projection()
            results[f"task_{i+1}_{task_type}"] = result
        elif task_type == "axis_angle":
            result = cs.axis_angle()
            results[f"task_{i+1}_{task_type}"] = result
        elif task_type == "area":
            result = cs.area()
            results[f"task_{i+1}_{task_type}"] = result
    return {"group_name":task_group["group_name"],"results":results}

#主函数
def main():
    # 读取JSON文件
    data =json.load(open('data(二维向量数据).json','r'))

    # 处理每个任务组
    list_task = []
    for task_group in data:
        result = processing_data(task_group)
        list_task.append(result)

    #以json的形式输出最终结果
    try:
        json_string = json.dumps(list_task, indent=4, default=default_dump)
        with open('ans_data.json', 'w', encoding='utf-8') as f:
            f.write(json_string)
        print("结果已成功保存到 ans_data.json")
    except Exception as e:
        print(f"写入文件时出错: {e}")

if __name__ == "__main__":
    main()