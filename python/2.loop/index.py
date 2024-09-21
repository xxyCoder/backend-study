# 条件语句
x = -1
if x < 0:
  print('<')
elif x == 0:
  print('==')
else:
  print('>')
  
# 循环
for i in range(2):
  print(i)

# 列表推导式
list = [i * 2 for i in range(10)]
print('list: ', list)

'''
# 生成器表达式
1. 返回值是一个generator对象
2. 数据量大的情况下，内存占比列表推导式少
  - 因为列表推导式是一次性生成所有数据，而生成器对象通过next函数获取下一个值
'''
gen = (i * 2 for i in range(10))
print('gen:', gen)
print('next:', next(gen))

'''
# 生成器函数
1. 返回值是一个generator对象
2. next函数执行到yield的位置停止，并将yield表达式的值作为next的返回值
'''
def generator(v):
  i = 1
  while i < 4:
    yield i ** v
    i += 1

gen2 = generator(2)
print('gen2: ', gen2)
print('gen2 next: ', next(gen2))
print('gen2 next: ', next(gen2))
print('gen2 next: ', next(gen2))
