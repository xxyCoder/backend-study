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

# 匿名函数
fc_lam = lambda arg1, arg2, **kwrags: print(arg1, arg2, type(kwrags))
fc_lam(1, 2, a=3,b=4)

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