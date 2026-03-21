```python
str1 = "I love you"
print(f"What i have said is{str1}")
```

    What i have said isI love you
    


```python
# //在python中是取余整符号
a = 15
b = a//2
print(f"the value of b is {b}")
```

    the value of b is 7
    


```python
# 在python中判断语句后要加:
T = True
F = False
if T :
    print("T")
elif F :
    print("F")
```

    T
    


```python
# 在python中int,float,str,bool可以相互转化，就像c语言中的强制类型转换一样即可
T = True
print(int(T))
```

    1
    


```python
#生成元祖有一种特殊的方法就是不要小括号直接用逗号相连接，就可以直接生成元祖，常用来替代f输出字符串
ans = 98
print(f"ans is {ans}")
print("ans is",ans)
```

    ans is 98
    ans is 98
    


```python
#元祖拆分法
#1.一次性创建多个变量
a,b,c = 1,2,3
print(c,b,a)
#2.快速交换两个变量的值
a,b = 1,2
b,a = a,b
print(a,b)
#3.容纳剩余元素，容器为列表，要加变量名前加上*号
values = 1,2,3,4,5,6
a,b,*rest = values
print(rest)
```

    3 2 1
    2 1
    [3, 4, 5, 6]
    


```python
# 在列表中下标可以是负数，-1表示的是列表的最后一个元素，-2是倒数第二个，依此类推
arr = [1,2,3,4,5,6]
print(arr[-1])
```

    6
    


```python
# list的切片，用来获取部分元素或是删除部分元素，每进行一次切分就会穿件一个变量
arr1 = [1,2,3,4,5,6,7]
print(arr[1 : 4]) #表示的是从索引一到索引四之前
print(arr[  : 4]) #表示的是从头开始到索引四之前
print(arr[  : : 2]) #表示的是每两个元素采样一次
print(arr[1 : -1: 2]) #表示的是消掉第一个元素和最后一个元素之后再按每两个元素采样一次
```

    [2, 3, 4]
    [1, 2, 3, 4]
    [1, 3, 5]
    [2, 4]
    


```python
# 在列表中添加元素直接用把想要添加的元素放进[]即可
arr2 = [1,2,3,4,5]
arr = arr + [100];
print(arr)
```

    [1, 2, 3, 4, 5, 6, 100]
    


```python
#字典添加元素，直接创建即可
dict_t = {'广东工业大学' : '双非',
          '华南理工大学' : '985'
          }
print(dict_t['广东工业大学'],dict_t['华南理工大学'])
dict_t['中山大学'] = '985'
print(dict_t['广东工业大学'],dict_t['华南理工大学'],dict_t['中山大学'])
# 删除元素用del
del dict_t['中山大学']
print(dict_t)
```

    双非 985
    双非 985 985
    {'广东工业大学': '双非', '华南理工大学': '985'}
    


```python
# list,tuple,set,dict可以像四个基本变量类型那样进行直接转化,字典整体在变成下面三个后会变成多个元组
list()
tuple()
set()
# 字典较为特殊，要使用zip()，第一个参数是键，第二个参数是值
dict_i = dict(zip(('a','b','c'),(1,2,3)))
print(dict_i)
```

    {'a': 1, 'b': 2, 'c': 3}
    


```python
# 在python中函数可以一次性返回多个值，在c、c++中只能return一个值
def culculate(v):
    '''加法和减法运算器'''  #这是文档字符串用来解释函数，在每个函数/类后面加上._doc_,就可以看函数的作用
    return v+v,v*v

x,y = culculate(5)
print(x,y)

#有与传入多个元素本质上是传递一个元组，所以在元组中的剩余元素也可以在函数中使用，要注意的是传入参数时要加上*，传出时不用
def print_arr(a,*b):
    return a,b

i,j = print_arr('jj','bb','hh','dd')
print(i,j)

# 还可以往函数中传递键值对参数,在参数前面加上**就可以表示一个字典参数
def jhj(x,y,**dict_p):
    dict_p['hhh'] = x
    dict_p['www'] = y
    return dict_p    

eva1 = jhj('ggg','ppp')
print(eva1)
eva2 = jhj('555','666',好的 = '777')  #新创立的键值对直接写上去即可，注意不能是数字
print(eva2)

# 为了减少传参的复杂性，可以预设某些参数的值
def evaluate(school,level = 't0前五'):
    massage = f"{school}是一个排名{level}的大学"
    return massage

p = evaluate('红岭中学') #使用默认值
print(p)
j = evaluate('广东工业大学',level = '倒数')
print(j)
```

    10 25
    jj ('bb', 'hh', 'dd')
    {'hhh': 'ggg', 'www': 'ppp'}
    {'好的': '777', 'hhh': '555', 'www': '666'}
    红岭中学是一个排名t0前五的大学
    广东工业大学是一个排名倒数的大学
    


```python
# 类本质上就是构造一个结构体(不考虑private/public的前提下)，然后结构体内有多个函数，各个函数之间的参数互通,一个类中包含一个__init__和多个自定义方法
# __init__方法本质上是把属性赋给变量

class Counter:
    def __init__ (self,a,b):
        '''a和b公共变量，也是self的属性'''
        self.a=a
        self.b=b
        #可以有默认值，不写进参数表里
        self.c = 'what can i say'
    
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def man(self):
        return self.c
    
jl = Counter(3,2)
print(jl.a,jl.b)
print(jl.add())
print(jl.c)
#修改默认值也很简单，直接修改即可
jl.c = 'i am a spiderman'
print(jl.c)
```

    3 2
    5
    what can i say
    i am a spiderman
    


```python
#继承，子类可以继承父类的所有属性和方法
class Counter2(Counter):
    def __init__(self,a,b):
        super().__init__(a,b)
    
    def mul(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
    
    def add(self):
        return self.a*2+self.b
    
test = Counter2(5,6)
print(test.sub())
print(test.mul())
print(test.add())
#如果1想在子类修改父类中的某个函数，直接在子类中定义一个新的同名函数,即可完成覆写或是叫做变异
```

    -1
    30
    16
    


```python
# 掠夺：继承只能继承一个类的方法，但如果想要得到很多其它类的方法，则需要掠夺功能。有了掠夺功能，一个类可以掠夺很多其它的类

class Amrc():
    def __init__(self,c,d):
        self.c = c
        self.d = d
        self.cnt = Counter(c,d) #掠夺Counter类的方法
    
    def mul(self):
        '''乘法'''
        return self.c * self.d
    def div(self):
        '''除法'''
        return self.c/self.d
    
test=Amrc(3,4)
print(test.mul())
print(test.cnt.add()) #抢来的方法,如果原始的类和掠夺后的类中都有同名的方法时，不用覆写，直接调用即可
```

    12
    7
    
