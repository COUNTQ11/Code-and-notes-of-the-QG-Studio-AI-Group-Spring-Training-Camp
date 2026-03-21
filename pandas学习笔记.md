```python
#作为标签库，Pandas对象在NumPy数组基础上给予其行列标签，有点类似于字典。
```


```python
import pandas as pd
import numpy as np
```


```python
#一.创建对象
```


```python
#1.1一维对象的创建
#方法一：字典创建法
dict_a = {'a':1,'b':2,'c':3,'d':4}
sr = pd.Series(dict_a)
print(sr)

#方法二：数组创建法：最直接的创建方法即直接给pd.Series()函数参数，其需要两个参数。第一个参数是值values（列表、数组、张量均可），第二个参数是键index（索引）
list_a = [1,2,3,4]
list_b = ['a','b','c','d']
sr = pd.Series(list_a,index=list_b)
print(sr)
```

    a    1
    b    2
    c    3
    d    4
    dtype: int64
    a    1
    b    2
    c    3
    d    4
    dtype: int64
    


```python
#1.2一维对象的属性
v = np.array([53,64,72,82])
k = ['1号','2号','3号','4号']
sr = pd.Series(v,index=k)
print(sr)
print(sr.values)
print(sr.index)
#可见，虽然Pandas对象的第一个参数values可以传入列表、数组与张量，但传进去后默认的存储方式是NumPy数组。一次可以得出：Pandas是建立在NumPy基础上的库，没有NumPy数组库就没有Pandas数据处理库。当想要Pandas退化为NumPy时，查看其values属性即可。
```

    1号    53
    2号    64
    3号    72
    4号    82
    dtype: int64
    [53 64 72 82]
    Index(['1号', '2号', '3号', '4号'], dtype='object')
    


```python
#1.3二维对象的创建
#方法一：字典创建法:用字典法创建二维对象时，必须基于多个Series对象，每一个Series就是一列数据，相当于对一列一列的数据作拼接。创建Series对象时，字典的键是index，其延展方向是竖直方向；创建DataFrame对象时，字典的键是columns，其延展方向是水平方向
v1=[53,64,72,82]
i=['1号','2号','3号','4号']
v2=['女','男','男','女']
sr1=pd.Series( v1, index=i)
sr2=pd.Series( v2,index=i)
df=pd.DataFrame( {'年龄':sr1,'性别':sr2 } )
print(df)
#如果sr1和sr2的index不完全一致，那么二维对象的index会取sr1与sr2的所有index，即取并集。

#方法二：数组创建法:最直接的创建方法即直接给pd.DataFrame函数参数，其需要三个参数。第一个参数是值values（数组），第二个参数是行标签index，第三个参数是列标签columns。其中，index和columns参数可以省略，省略后即从0开始的顺序数字。
v=np.array( [ [53,'女'], [64,'男'], [72,'男'], [82,'女'] ] )
i=['1号','2号','3号','4号']
c=['年龄','性别']
df1 = pd.DataFrame(v,index=i,columns=c)
print(df1)
```

        年龄 性别
    1号  53  女
    2号  64  男
    3号  72  男
    4号  82  女
        年龄 性别
    1号  53  女
    2号  64  男
    3号  72  男
    4号  82  女
    


```python
#1.4二维对象的属性
print(df1.values)
print(df1.index)
print(df1.columns)
#当想要Pandas退化为NumPy时，查看其values属性即可。
arr_a = df1.values
print(arr_a)
#提取第[0]列，并转化为一个整数型数组
arr_b=arr_a[:,0].astype(int)
print(arr_b)
```

    [['53' '女']
     ['64' '男']
     ['72' '男']
     ['82' '女']]
    Index(['1号', '2号', '3号', '4号'], dtype='object')
    Index(['年龄', '性别'], dtype='object')
    [['53' '女']
     ['64' '男']
     ['72' '男']
     ['82' '女']]
    [53 64 72 82]
    


```python
#二、对象的索引:Pandas的索引分为显式索引与隐式索引。显式索引是使用Pandas对象提供的索引，而隐式索引是使用数组本身自带的从0开始的索引。现假设代码中的索引是整数，这个时候显式索引和隐式索引可能会出乱子。于是，Pandas作者发明了索引器loc（显式）与iloc（隐式），手动告诉程序 这句话是显式索引还是隐式索引。
```


```python
#2.1一维对象的索引
#（1）访问元素
v = [12,25,36,51]
k =['一号','二号','三号','四号']
sr_1 = pd.Series(v,index=k)
print(sr_1)
#显示索引
print(sr_1.loc['二号'])
print(sr_1.loc[['一号','三号']])
#隐式索引
print(sr_1.iloc[1])
print(sr_1.iloc[[0,2]])
#（2）访问切片:使用显式索引时，'1号':'3号'可以涵盖最后一个'3号'，但隐式与之前一样是到右索引的前一个
v = [53,64,72,82]
k = ['1号','2号','3号','4号']
sr_2 = pd.Series(v,index=k)
#显式索引
print(sr_2['1号':'3号'])
#隐式索引
print(sr_2[0:3])
```

    一号    12
    二号    25
    三号    36
    四号    51
    dtype: int64
    25
    一号    12
    三号    36
    dtype: int64
    25
    一号    12
    三号    36
    dtype: int64
    1号    53
    2号    64
    3号    72
    dtype: int64
    1号    53
    2号    64
    3号    72
    dtype: int64
    


```python
#二维对象的索引：在二维对象中，索引器不能去掉，否则会报错，因此必须适应索引器的存在。
#（1）访问元素
i=['1号','2号','3号','4号']
v1=[53,64,72,82]
v2=['女','男','男','女']
sr_3 = pd.Series(v1,index=i)
sr_4 = pd.Series(v2,index=i)
sr_5 = pd.DataFrame({'年龄':sr_3,'性别':sr_4})
#显式
print(sr_5.loc['1号','年龄'])
print(sr_5.loc[['1号','3号'],['性别','年龄']])
#隐式
print(sr_5.iloc[0,0])
print(sr_5.iloc[[0,2],[1,0]])
#（2）访问切片
v=[ [53,'女'], [64,'男'], [72,'男'], [82,'女'] ]
i=['1号','2号','3号','4号']
c=['年龄','性别']
sr_6 = pd.DataFrame(v,index=i,columns=c)
print(sr_6)
#显式
print(sr_6.loc['1号':'3号','年龄'])
print(sr_6.loc['3号',:])
print(sr_6.loc[:,'年龄'])
#隐式
print(sr_6.iloc[0:3,0])
print(sr_6.iloc[2,:])
print(sr_6.iloc[:,0])
```

    53
       性别  年龄
    1号  女  53
    3号  男  72
    53
       性别  年龄
    1号  女  53
    3号  男  72
        年龄 性别
    1号  53  女
    2号  64  男
    3号  72  男
    4号  82  女
    1号    53
    2号    64
    3号    72
    Name: 年龄, dtype: int64
    年龄    72
    性别     男
    Name: 3号, dtype: object
    1号    53
    2号    64
    3号    72
    4号    82
    Name: 年龄, dtype: int64
    1号    53
    2号    64
    3号    72
    Name: 年龄, dtype: int64
    年龄    72
    性别     男
    Name: 3号, dtype: object
    1号    53
    2号    64
    3号    72
    4号    82
    Name: 年龄, dtype: int64
    


```python
#三、对象的变形
```


```python
#3.1对象的转置：有时候提供的大数据很畸形，行是特征，列是个体，这必须要先进行转置。
v=[ [53,64,72,82],['女','男','男','女']]
i=['年龄','性别']
c=['1号','2号','3号','4号']
df=pd.DataFrame( v, index=i, columns=c )
print(df)
df = df.T
print(df)
```

        1号  2号  3号  4号
    年龄  53  64  72  82
    性别   女   男   男   女
        年龄 性别
    1号  53  女
    2号  64  男
    3号  72  男
    4号  82  女
    


```python
#3.2对象的翻转
v=[ [53,64,72,82],['女','男','男','女']]
i=['年龄','性别']
c=['1号','2号','3号','4号']
df=pd.DataFrame( v, index=i, columns=c )
#中括号里的内容类似于numpy中的.arange，逗号前是行逗号后是列第一个冒号是从哪到哪，第二个冒号后是步长
df = df.iloc[:,::-1]#翻转列
print(df)
df = df.iloc[::-1,:]#翻转行
print(df)
```

        4号  3号  2号  1号
    年龄  82  72  64  53
    性别   女   男   男   女
        4号  3号  2号  1号
    性别   女   男   男   女
    年龄  82  72  64  53
    


```python
#3.3对象的重塑考虑到对象是含有行列标签的，.reshape()已不再适用，因此对象的重塑没有那么灵活。但可以做到将sr并入df，也可以将df割出sr。
i=['1号','2号','3号','4号']
v1=[10,20,30,40]
v2=['女','男','男','女']
v3=[1,2,3,4]
sr1=pd.Series( v1, index=i)
sr2=pd.Series( v2, index=i)
sr3=pd.Series( v3, index=i)
df=pd.DataFrame({'年龄':sr1,'性别':sr2})
print(df)
df['牌照']=sr3
print(df)
sr4 = df.loc[:,'年龄']
print(sr4)
```

        年龄 性别
    1号  10  女
    2号  20  男
    3号  30  男
    4号  40  女
        年龄 性别  牌照
    1号  10  女   1
    2号  20  男   2
    3号  30  男   3
    4号  40  女   4
    1号    10
    2号    20
    3号    30
    4号    40
    Name: 年龄, dtype: int64
    


```python
#3.4对象的拼接
#（1）一维对象的合并
v1=[10,20,30,40]
v2=[40,50,60]
k1=['1号','2号','3号','4号']
k2=['4号','5号','6号']
sr1=pd.Series( v1, index=k1 )
sr2=pd.Series( v2, index=k2 )
print(sr1)
print(sr2)
sr3=pd.concat([sr1,sr2])
print(sr3)
#值得注意的是，Out[3]的键中出现了两个“4号”，这是因为Pandas对象的属性，放弃了集合与字典索引中“不可重复”的特性，实际中，这可以拓展大数据分析与处理的应用场景。那么，如何保证索引是不重复的呢？对对象的属性.index或.columns使用.is_unique即可检查，返回True表示行或列不重复，False表示有重复。
print(sr3.index.is_unique)
#（2）一维对象与二维对象的合并:一维对象与二维对象的合并，即可理解为：给二维对象加上一列或者一行。因此，不必使用pd.concat()函数.
v1=[10,20,30]
v2=['女','男','男']
sr1=pd.Series( v1, index=['1号','2号','3号'])
sr2=pd.Series( v2, index=['1号','2号','3号'])
df=pd.DataFrame( {'年龄':sr1,'性别':sr2 } )
print(df)
df.loc[:,'牌照']=[1,2,3]
print(df)
df.loc['4号',:]=[40,'女',4]
print(df)
```

    1号    10
    2号    20
    3号    30
    4号    40
    dtype: int64
    4号    40
    5号    50
    6号    60
    dtype: int64
    1号    10
    2号    20
    3号    30
    4号    40
    4号    40
    5号    50
    6号    60
    dtype: int64
    False
        年龄 性别
    1号  10  女
    2号  20  男
    3号  30  男
        年龄 性别  牌照
    1号  10  女   1
    2号  20  男   2
    3号  30  男   3
          年龄 性别   牌照
    1号  10.0  女  1.0
    2号  20.0  男  2.0
    3号  30.0  男  3.0
    4号  40.0  女  4.0
    


```python
#（3）二维对象的合并
v1=[ [10,'女'], [20,'男'], [30,'男'], [40,'女'] ]
v2=[ [1,'是'], [2,'是'], [3,'是'], [4,'否'] ]
v3=[ [50,'男',5,'是'], [60,'女',6,'是'] ]
i1=['1号','2号','3号','4号']
i2=['1号','2号','3号','4号']
i3=['5号','6号']
c1=['年龄','性别']
c2=['牌照','ikun']
c3=['年龄','性别','牌照','ikun']
df1=pd.DataFrame( v1, index=i1, columns=c1)
df2=pd.DataFrame( v2, index=i2, columns=c2)
df3=pd.DataFrame( v3, index=i3, columns=c3)
#合并列对象（添加列特征，打断了了行axis=1）
df = pd.concat([df1,df2],axis=1)
print(df)
##合并行对象（添加行个体,打断了列axis=0）
df_1 = pd.concat([df,df3],axis=0)
print(df_1)
```

        年龄 性别  牌照 ikun
    1号  10  女   1    是
    2号  20  男   2    是
    3号  30  男   3    是
    4号  40  女   4    否
        年龄 性别  牌照 ikun
    1号  10  女   1    是
    2号  20  男   2    是
    3号  30  男   3    是
    4号  40  女   4    否
    5号  50  男   5    是
    6号  60  女   6    是
    


```python
#四、对象的运算
```


```python
#4.1对象与系数之间的运算
sr=pd.Series([53,64,72], index=['1号','2号','3号'])
v=[ [53,'女'], [64,'男'], [72,'男']]
df=pd.DataFrame( v, index=['1号','2号','3号'], columns=['年龄','性别'])
print(df)
sr=sr+10
print(sr)
df['年龄']=df['年龄']+10
print(df.loc[:,'年龄'])
```

        年龄 性别
    1号  53  女
    2号  64  男
    3号  72  男
    1号    63
    2号    74
    3号    82
    dtype: int64
    1号    63
    2号    74
    3号    82
    Name: 年龄, dtype: int64
    


```python
#4.2对象与对象之间的运算对象做运算，必须保证其都是数字型对象，两个对象之间的维度可以不同。
#二维对象之间的运算
v1=[ [10,'女'], [20,'男'], [30,'男'], [40,'女'] ]
v2=[1,2,3,6]
i1 = ['1号','2号','3号','4号'];c1= ['年龄','性别']
i2 = ['1号','2号','3号','6号'];c2= ['牌照']
df1=pd.DataFrame( v1, index=i1, columns=c1)
df2=pd.DataFrame( v2, index=i2, columns=c2)
print(df1)
print(df2)
#加法
df1['加法']=df1['年龄']+df2['牌照']
print(df1)
#减法、乘法、除法、幂方
df1['减法']=df1['年龄']-df2['牌照']
df1['乘法']=df1['年龄']*df2['牌照']
df1['除法']=df1['年龄']/df2['牌照']
df1['幂方']=df1['年龄']**df2['牌照']
print(df1)
#使用np.abs()、np.cos()、np.exp()、np.log()等数学函数时，会保留索引；Pandas中仍然存在布尔型对象，用法与NumPy无异，会保留索引。
```

        年龄 性别
    1号  10  女
    2号  20  男
    3号  30  男
    4号  40  女
        牌照
    1号   1
    2号   2
    3号   3
    6号   6
        年龄 性别    加法
    1号  10  女  11.0
    2号  20  男  22.0
    3号  30  男  33.0
    4号  40  女   NaN
        年龄 性别    加法    减法    乘法    除法       幂方
    1号  10  女  11.0   9.0  10.0  10.0     10.0
    2号  20  男  22.0  18.0  40.0  10.0    400.0
    3号  30  男  33.0  27.0  90.0  10.0  27000.0
    4号  40  女   NaN   NaN   NaN   NaN      NaN
    


```python
#五、对象的缺失值
```


```python
#5.1发现缺失值:发现缺失值使用.isnull()方法
v=[ [None,1], [64,None], [72,3], [82,4] ]
i=['1号','2号','3号','4号']
c=['年龄','牌照']
df=pd.DataFrame( v, index=i, columns=c)
print(df)
print(df.isnull())
#除了.isnull()方法，还有一个与之相反的.notnull()方法，但不如在开头加一个非号“~”即可。
```

          年龄   牌照
    1号   NaN  1.0
    2号  64.0  NaN
    3号  72.0  3.0
    4号  82.0  4.0
           年龄     牌照
    1号   True  False
    2号  False   True
    3号  False  False
    4号  False  False
    


```python
#5.2剔除缺失值:剔除缺失值使用.dropna()方法，一维对象很好剔除；二维对象比较复杂，要么单独剔除df中含有缺失值的行，要么剔除df中含有缺失值的列。
#剔除一维对象的缺失值
v=[53,None,72,82]
k=['1号','2号','3号','4号']
sr=pd.Series( v, index=k )
print(sr)
sr=sr.dropna()
print(sr)
#剔除二维对象的缺失值
v=[ [None,None], [64,None], [72,3], [82,4] ]
i=['1号','2号','3号','4号']
c=['年龄','牌照']
df=pd.DataFrame( v, index=i, columns=c)
print(df)
print(df.dropna()) #只要存在缺失值的行全部被剔除
print(df.dropna(how='all')) #只剔除值全是NaN的元素
```

    1号    53.0
    2号     NaN
    3号    72.0
    4号    82.0
    dtype: float64
    1号    53.0
    3号    72.0
    4号    82.0
    dtype: float64
          年龄   牌照
    1号   NaN  NaN
    2号  64.0  NaN
    3号  72.0  3.0
    4号  82.0  4.0
          年龄   牌照
    3号  72.0  3.0
    4号  82.0  4.0
          年龄   牌照
    2号  64.0  NaN
    3号  72.0  3.0
    4号  82.0  4.0
    


```python
#5.3填补缺失值:填充缺失值使用.fillna()方法
v=[ [None,None], [64,None], [72,3], [82,4] ]
i=['1号','2号','3号','4号'];c=['年龄','牌照']
df=pd.DataFrame( v, index=i, columns=c)
print(df)
print(df.fillna(0)) #把缺失值全部填为0
print(df.fillna(np.mean(df))) #把缺失值填为该列的均值
print(df.ffill()) #把缺失值填成这一列的前一个数,front fill
print(df.bfill()) #把缺失值填成这一列的后一个数,back fill
```

          年龄   牌照
    1号   NaN  NaN
    2号  64.0  NaN
    3号  72.0  3.0
    4号  82.0  4.0
          年龄   牌照
    1号   0.0  0.0
    2号  64.0  0.0
    3号  72.0  3.0
    4号  82.0  4.0
          年龄    牌照
    1号  45.0  45.0
    2号  64.0  45.0
    3号  72.0   3.0
    4号  82.0   4.0
          年龄   牌照
    1号   NaN  NaN
    2号  64.0  NaN
    3号  72.0  3.0
    4号  82.0  4.0
          年龄   牌照
    1号  64.0  3.0
    2号  64.0  3.0
    3号  72.0  3.0
    4号  82.0  4.0
    
