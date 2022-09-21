class Student:   #Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace='西安'   #直接写在类里的变量，称为类属性
    def __init__(self,name,age):   #初始化方法
        self.name=name   #self.name 称为实体属性，进行了一个赋值的操作，将局部变量name的值赋给实体属性
        self.age=age
    #实例方法：
    def eat (self):   #实例方法的self不能省略
        print('学生在吃饭。。。')
    #静态方法：
    @staticmethod
    def method():   #静态方法的（）中啥都没有，不允许写self
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法：
    @classmethod
    def cm(cls):   #类方法的（）中要写cls
        print('我是类方法，因为我使用了classmethod进行修饰')

#在类之外定义的称为函数，在类之内定义的称为方法
def drink ():
    print('喝水')


#创建Student类的对象：
stu1 = Student('张三',20)
stu1.eat()    #对象名.方法名（）
print(stu1.name)
print(stu1.age)

print('--------------------------')
Student.eat(stu1)   #33行与28行代码功能相同，都是使用student中的eat方法
                    #类名.方法名（类的对象）-->实际上就是方法定义处的self

#类属性的使用方法：
print(Student.native_pace)   #使用类名去调用
stu1 = Student('张三',20)
stu2 = Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = '北京'
print(stu1.native_pace)
print(stu2.native_pace)

print('-------------类方法的使用方法----------------')
Student.cm()
print('-------------静态方法的使用方法----------------')
Student.method()

#动态绑定属性和方法：
class student:
    def __init__(self,name,age):   #定义初始化方法
        self.name = name    #将局部变量的值name赋给实例变量self.name      self.name、self.age是 student类所有对象所共有的
        self.age = age
    def eat(self):   #定义了一个方法
        print(self.name + '在吃饭！')

stu1 = student('张三',20)   #创建类的对象
stu2 = student('李四',30)
print('--------------为stu2动态的绑定性别属性------------------')
stu2.gender = '女'   #为stu2动态的绑定性别属性   该属性只是stu2这个对象所特有的
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)
# print(stu1.name,stu1.age,stu1.gender)    #AttributeError: 'student' object has no attribute 'gender'程序报错，stu1没有gender这个属性
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的称为函数！')
stu1.show = show    #动态绑定方法（给stu1动态绑定show方法）
stu1.show()
# stu2.show()  #AttributeError: 'student' object has no attribute 'show'  报错，因为stu2并没有绑定show方法
'''
类属性、类方法、静态方法都是类名打点去调用【类名.方法名】
实例方法是对象名打点去调用【对象名.方法名】（1、stu=student（）
                                         stu.eat()
                                      2、student.eat(stu)
                                        ）
'''

class cb:
    def __init__(self,name,age,gender,salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.__salary = salary   #工资不希望在类的外部被使用，所以添加了两个'_'
    def show(self):
        print(self.name,self.age,self.gender,self.__salary)

cb1 = cb('陈斌',30,'男',22000)
cb1.show()
#在类的外部使用name、age、gender、salary
print(cb1.name)
print(cb1.age)
print(cb1.gender)
# print(cb1.__salary)   # 不想让在外部使用，所以在类外部使用时程序报错 （AttributeError: 'cb' object has no attribute '__salary'）
print(dir(cb1))
print(cb1._cb__salary)   #在类的外部可以通过 _cb__salary 进行访问不希望被访问的属性  （对象名._类名__不需要访问的实例属性）

#继承：
'''
1、如果一个类没有继承任何类，则默认继承object
2、python支持多继承
3、定义子类时，必须在其构造函数中调用父类的构造函数
'''
class person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class cb2(person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no

class cb3(person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
#创建学生类和教师类的对象：
stu = cb2('张三',20,'1001')
teacher = cb3('陈斌',34,10)
#调用person的info方法：
stu.info()
teacher.info()

#多继承实例：
'''
a、b都继承与object，c继承a、b
'''
class a(object):
    pass
class b(object):
    pass
class c(a,b):
    pass

#方法重写：
class person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class cb2(person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
    def info(self):
        super().info()
        print(self.stu_no)

class cb3(person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
    def info(self):
        super().info()
        print(self.teachofyear)
#创建学生类和教师类的对象：
stu = cb2('张三',20,'1001')
teacher = cb3('陈斌',34,10)
#调用person的info方法：
stu.info()
teacher.info()

#object类：
'''
1、object类是所有类的父类，因此所有类都有object类的属性和方法
2、内置函数dir（）可以查看指定对象所有的属性
3、object有一个__str__()方法，用于返回一个对于"对象的描述"，对应于内置函数str（）经常用于print（）方法，棒我们查看对象的信息，所以我们经常
会对__str__（）进行重写
'''
class cb4:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):   # 重写父类的方法
        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)
stu = cb4('陈斌',30)
print(dir(stu))   #用dir（）这个函数查看stu这个对象所具有的所有属性和方法（不是我们定义的而是从object中继承过来的）
print(stu)   # 默认会调用__str__（）的方法  <__main__.cb4 object at 0x10639dac0>对象的内存地址
print(type(stu))   # <class '__main__.cb4'>

#多态：
class animal(object):
    def eat(self):
        print('动物要吃东西')
class dog(animal):
    def eat(self):
        print('狗吃肉')
class cat(animal):
    def eat(self):
        print('猫吃鱼')
class person(object):
    def eat(self):
        print('人吃五谷杂粮')
#定义一个函数
def fun(obj):
    obj.eat()
#开始调用函数
fun(cat())
fun(dog())
fun(animal())
fun(person())   #person与dog、cat、animal都没有继承关系，但是有eat（）方法，也会调用eat方法

#特殊的属性：
class a(object):
    pass
class b(object):
    pass
class c(a,b):
    def __init__(self,name,age):
        self.name = name
        self.age = age
#创建c类的对象
x = c('jack',20)   #x是c类型的属性对象
print(x.__dict__)   #{'name': 'jack', 'age': 20}   查看实例对象的属性（得倒的是实例对象的属性字典）
print(c.__dict__)   #{'__module__': '__main__', '__init__': <function c.__init__ at 0x1009a6a60>, '__doc__': None}
                    # 如果是类对象的话会看到属性、方法的字典（方法是类对象当中的，实例对象只能负责调用）
print(x.__class__)   #<class '__main__.c'>  输出了对象所属的类
print(c.__bases__)   #(<class '__main__.a'>, <class '__main__.b'>) c类父类的类型元素
print(c.__base__)    #<class '__main__.a'> 类的基类
print(c.__mro__)    #(<class '__main__.c'>, <class '__main__.a'>, <class '__main__.b'>, <class 'object'>) 类的层次结构
print(a.__subclasses__())    #[<class '__main__.c'>] 子类的列表

#特殊的方法：
a = 20
b = 100
c = a+b   #两个整数类型的对象的相加操作
d = a.__add__(b)   #上面c=a+b的底层其实是调用了a.__add__(b)该方法
print(c)
print(d)
class e:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)
e1 = e('张三')
e2 = e('jack')
s = e1 + e2   #实现了两个对象的加法运算（因为在e类中编写了 __add__（）特殊方法）
print(s)   #TypeError: unsupported operand type(s) for +: 'e' and 'str'  如果非要让其相加可以写上238-239行的代码即可（张三jack）
s = e1.__add__(e2)   #实现了两个对象的加法运算（因为在e类中编写了 __add__（）特殊方法）
print(s)

lst = [11,22,33,44]
print(len(lst))   #len（）是内置函数
print(lst.__len__())
print(len(e1))   #TypeError: object of type 'e' has no len()  实现计算对象的长度（因为在e类中编写了 __len__（）特殊方法）
print(len(e2))

class person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))   #new方法创建对象
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age
print('object这个类对象的ID为：{0}'.format(id(object)))
print('person这个类对象的ID为：{0}'.format(id(person)))
#创建person类的实例对象
p1 = person('cb',30)
print('p1这个person类的实例对象的ID为：{0}'.format(id(p1)))
'''
new在前是创建对象，init在后是为这个对象的实例属性进行赋值，最后将创建的对象放到了p1当中进行存储
'''

# import schedule
# import time
# def job():
#     print('哈哈----爱你哦！')
# schedule.every(3).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(2)

'''
file = open('333.txt','r')
print(file.readlines())
file.close()
#以下代码如果文件不存在时，会自动创建文件并将内容写入文件当中，如果再次执行以下代码将会把文件中已有的内容进行替换
file = open('test.txt','w')
file.write('你好python 2022-9-20')
file.close()
#如果将参数换成a的话，将会在文件的末尾进行追加内容（如果文件不存在会自动创建文件）
file = open('test.txt','a')
file.write('你好python 2022-9-20 222')
file.close()
#copy二进制文件（图片）
src_file = open('海滩比基尼.jpeg','rb')
target_file = open('美女.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

file = open('test.txt','r')
print(file.read())   #将文件中的内容全部读取出来
file = open('test.txt','r')
print(file.read(6))   #读取文本文件当中的6个字符的长度内容
file = open('test.txt','r')
print(file.readline())   #从文本文件中读取一行内容
file = open('test.txt','r')
print(file.readlines())   #把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
file = open('c.txt','a')
file.write('hello')   #将字符串写到文件当中
lst = ['java','go','python']
file.writelines(lst)   #将列表中的内容写进文件当中，不添加换行符
file.close()
file = open('c.txt','r')
file.seek(2)
print(file.read())   #
print(file.tell())   #返回文件指针的当前位置
file.close()
'''

#with语句：(用with的方法实现文件的复制，不需要写关闭文件的程序了，with语句可以自动管理上下文资源，不论什么原因跳出with快，都能确保文件正常
# 的关闭，以此来达到释放资源的目的)
with open('美女.png','rb') as src_file:
    with open('copy2logo.png','wb') as target_file:
        target_file.write(src_file.read())

'''
#os模块：
import os
os.system('国际象棋.dmg')
os.system('notepad.dmg')
#还可以直接调用可执行文件
os.startfile('C:\\program Files\\Tencent\QQ\\Bin\\qq.dmg')
'''
import os
print(os.getcwd())   #打印当前的操作路径/目录
lst = os.listdir('../python_work')   #打印python_work目录中的所有文件
print(lst)   #打印python_work目录中的所有文件 （返回指定路径下的文件和目录信息）
# os.mkdir('newdir')   #mkdir(path[,mode]) 创建目录
# os.makedirs('A/B/C')   #创建多级目录 （a目录下有b目录，b目录下有从c目录）
# os.rmdir('newdir')   #删除xxx路径下的目录
# os.removedirs('A/B/C')   #删除多级目录
# os.chdir('E:\\xxx\\xxx')   #将path设置为当前工作目录
# print(os.getcwd())

import os.path
print(os.path.abspath('Class.py'))   #abspath(path) 用于获取文件/目录的绝对路径
print(os.path.exists('Class.py'),os.path.exists('Class111.py'))   #exists（path）用于判断文件或目录是否存在，存在返回Ture，否则返回False
# print(os.path.join('E:\\xxx\\xxx','Class111.py'))   #join（path，name） 将目录与目录或者文件名凭借起来
print(os.path.splitext('Class.py'))    #('Class', '.py')   splitext（） 分离文件名和扩展名
print(os.path.basename('/Users/chenbin/Desktop/python_work/Class.py'))    #Class.py   basename（path） 从一个目录中提取文件名
print(os.path.dirname('/Users/chenbin/Desktop/python_work/Class.py'))    #/Users/chenbin/Desktop/python_work     dirname（path）
                                                                         # 从一个路径中提取文件路径，不包括文件名
print(os.path.isdir('/Users/chenbin/Desktop/python_work/Class.py'))   #False     isdir（path)用于判断是否为路径
print(os.path.split('/Users/chenbin/Desktop/python_work/Class.py'))   #('/Users/chenbin/Desktop/python_work', 'Class.py')
                                                                      # 将文件的路径和文件名进行拆分

#列出指定目录下的所有的python文件
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

#遍历当前目录下的所有文件：
import os
path = os.getcwd()
lst_files = os.walk(path)
for dirpath,dirname,filename in lst_files:
    '''
    print(dirpath)
    print(dirname)
    print(filename)
    print('----------------------------')
    '''
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print('----------------------------')
