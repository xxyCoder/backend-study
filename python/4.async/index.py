def foo():
  print('foo start')
  # bar() 切换
  print('foo end')

def bar():
  print('bar start')
  # foo() 切换
  print('bar end')

# 上面这种切换会造成死循环，如果想要切换时候回到上次离开位置则需要使用协程
# 协程拥有自己的寄存器上下文和栈，调度切换能够保存和恢复（进入上次离开时所处的逻辑位置）

import asyncio

# 非function，而是coroutine object
async def work(i):
  print(f"work {i} start")
  await asyncio.sleep(i)
  print(f"work {i} end")
  return i

def callback(task):
  print(task.done(), task.result())

# event loop控制协程对象执行
tasks= [
  asyncio.ensure_future(work(1)),
  asyncio.ensure_future(work(2))
]
tasks[0].add_done_callback(callback)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 新语法，对event loop封装
async def main():
  tasks = [
    asyncio.create_task(work(1)),
    asyncio.create_task(work(2))
  ]
  ret = await asyncio.gather(*tasks)
  print('all end', ret)
  
# 相当于get_event_loop()，紧接着wait(main)，最后loop.close()
asyncio.run(main())