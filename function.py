def calc (a,b):   #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
    c = a + b
    return c
result = calc(10,20)   #10,20称为实际参数，简称实参，实参的位置是在函数的调用处
print(result)

res = calc(b=10,a=20)   #等号左边的变量名称，称为关键字参数.
print(res)

def fun(arg1,arg2):
    print('arg1=',arg1)   #arg1= 11
    print('arg2=',arg2)   #arg2= [22, 33, 44]
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)   #arg1= 100
    print('arg2=', arg2)   #arg2= [22, 33, 44, 10]

n1 = 11
n2 = [22,33,44]
print(n1)   #11
print(n2)   #[22, 33, 44]
fun(n1,n2)   #将位置传惨 ，arg1，arg2，是函数定义处的形参，n1，n2是函数调用处的实参。  总结：实参名称和形参明灿可以不一致。
'''在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改过程中不会影响实参的值（arg1修改为100，不会影响n1的值）
如果是可变对象，在函数体的修改过程中会影响实参的值（arg2的修改，append（10），会影响n2的值'''
print(n1)   #11
print(n2)   #[22, 33, 44, 10]

def fun1 (num):
    odd = []
    even = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
#函数的调用.
lst = [10,29,34,23,44,53,55]
a = fun1(lst)
print(a)
'''
函数的返回值
  （1）如果函数没有返回值（函数执行完毕之后，不需要给调用处提供数据）return可以省略不写
  （2）函数的返回值如果是一个，直接返回愿类型
  （3）函数的返回值如果是多个，返回的结果为元组
'''
def fun2():
    print('hello')   #hello

fun2()

def fun3():
    return 'hello'

res = fun3()
print(res)   #hello

def fun4():
    return 'hello','world'

print(fun4())   #('hello', 'world')

'''函数在定义时，是否需要写返回值视情况而定'''

'''
函数定义默认值参数
  函数定义时，给形式参数设置默认值，只有与默认值不符合的时候才需要传递实参
'''
def fun5(a,b=10):
    print(a,b)
#函数的调用
fun5(100)   #只传一个参数，b采用默认值，将参数传给了a    100 10
fun5(20,30)   #传两个参数，30将默认值10替换     20 30



one = (1, 2, 3)
two = ('a', 'b')
print(one+two)

lists = [1, 2, 3]
lists.insert(2, [7,8,9])
print(lists)

strs = 'abcd12efg'
print(strs.upper().title())


def chanageList(nums):
    nums.append('c')
    print("nums", nums)
str1 = ['a', 'b']
# 调用函数
chanageList(str1)
print("str1", str1)

a = 100
b = 14
print(divmod(a, b))


for i in range(5):
    i+=1
    print("-------")
    if i==3:
      continue
    print(i)

nl = [1, 2, 5, 3, 5]

nl.append(4)
nl.insert(0, 7)
nl.sort()

print(nl)


trupls = [(1, 2), (2, 3, 4), (4, 5)]
lists = []
for tru in trupls:
    for num in tru:
        lists.append(num)
print(lists)


lists = [1, 2, 3, 4, 5, 6]
print(lists[6:])


res = 0
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and i != k and j != k:
                res += 1
print(res)
