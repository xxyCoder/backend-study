'''
# 函数
1. def声明一个函数，def是一个可执行语句，意味着函数被调用前都是不存在的，只有被调用时才会创建一个新的函数对象
2. 参数设置默认值，但是一个参数设置了默认值，其后面的参数也需要有
3. 不能在函数内部随意改变全局变量的值，因为默认函数内部的变量为局部变量，对于全局和局部同名，局部覆盖全局
4. 内部函数能够访问外部函数，却无法修改，需要通过nonlocal关键字声明
5. 调用函数时可以指定参数名赋值
6. *args用于接收多个任意数量的参数，收集到一个元组中，**kwargs则是收集到一个字典中
'''

global_var = 1

def basic_fc(name, age = 22, addr = 'China', *args):
  print('func', type(args))
  global global_var
  global_var += 1
  def inner_fc():
    nonlocal age
    age += 1
    print('inner fc: ', name, age, addr, global_var)
    return age
  return inner_fc

fc = basic_fc(age=21, name='xxyCoder')
fc()

# *args和**kwrags

def func_args(*args):
  print(args, type(args))
func_args(1, 2, 3)

def func_kwrags(**kwrags):
  print(kwrags, type(kwrags))
func_kwrags(name="xxyCoder", age=17)

# nonlocal
def func_1():
  a = 20
  def func_2():
    def func_3():
      nonlocal a
      a = 30
      print(a, 'func_3')
    func_3()
    print(a, 'func_2')
  func_2()

func_1()

# 匿名函数
fc_lam = lambda arg1, arg2, **kwrags: print(arg1, arg2, type(kwrags))
fc_lam(1, 2, a=3,b=4)
fc_lam_no_arg = lambda : print('no args')

'''
# 协程
1. async声明异步函数，调用异步函数得到协程对象
2. await调用异步函数
3. asyncio.create_task创建任务，asyncio.run运行异步任务
'''
import asyncio
async def sleep(time):
  await asyncio.sleep(time)

async def async_fc():
  tasks = [asyncio.create_task(sleep(i)) for i in range(4)]
  # for task in tasks:
  #   await task
  await asyncio.gather(*tasks)
  print('async func')

a_fc = async_fc()
print('async: ', a_fc)
asyncio.run(async_fc())

'''
# 装饰器
1. @为语法糖，相当于greet=my_decorator(greet)
2. 通过functools.wraps包裹原函数，可以帮助保留原函数的元信息
'''
import functools
def my_decorator(func):
  @functools.wraps(func)
  def wrapper(message):
    print('wrapper!!!')
    func(message)
  return wrapper

@my_decorator
def greet(message):
  print('greet, hi!', message)
greet('xxyCoder')

# 类装饰器
class Count():
  def __init__(self, func) -> None:
    self.cnt = 0
    self.func = func
  def __call__(self, *args, **kwds):
    self.cnt += 1
    return self.func(*args, **kwds)

'''
# 类
1. class声明一个类
2. __开头的属性是私有的，与函数在一处声明的是静态属性
3. init表示构造函数，@staticmethod修饰的是静态方法，@classmethod修饰的是类方法，用于帮忙创建类实例
'''
class Document():
  STATIC = 'static upper'
  static = 'static lower'
  def __new__(cls, *args, **kwrags):
    print(cls, args, kwrags, 'new method')
    return super().__new__(cls)
  def __init__(self, title, author, content) -> None:
    print('init document')
    self.title = title
    self.author = author
    self.__content = content
  def see(self):
    print('content: ', self.__content)
  @staticmethod
  def show_static():
    print('class static: ', Document.STATIC, Document.static)
  @classmethod
  def create_empty_doc(cls, title, author):
    return cls(title=title, author = author, content = "")
    
doc = Document('py class', 'xxyCoder', 'self')
doc.see()
Document.show_static()

empty_doc = Document.create_empty_doc('empty', 'xxyCoder')
empty_doc.see()

# 继承
class DOCX(Document):
  def __init__(self, title, author, content, is_read) -> None:
    self.__is_read = is_read
    self.__content = "override " + content
    super().__init__(title, author, content)
  def see(self):
    print('sub class see')
    return super().see()
    
    
dc = DOCX('docx', 'xxy', 'none', False)
dc.see()

# 抽象
from abc import ABCMeta, abstractmethod
class AB(metaclass=ABCMeta):
  @abstractmethod
  def see(self):
    pass
  
# 异常
class MyError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return ("{} is invalid".format(repr(self.value)))
try:
  raise MyError(1)
except (ValueError, IndexError) as err:
  print('value or index error')
except MyError as err:
  print(err)
except:
  print('unknow error')