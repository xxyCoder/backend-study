"""
# 基本数据类型
1. int
  - py3中理论上位数无限，py2位数受机器位数限制
  - 转float：末尾添加.0，转str：添加引号
2. float
  - 64位
  - 转int：截取小数位，转str：添加引号
3. str
  - 不可变的，但在2.5之后会检测该字符串是否有其他被引用，如果没有则尝试原地扩充字符串大小
  - 转数值类型：不能转换则报错
4. bool
  - True和Flase两种取值
5. None
  - 表示空值
- 没有赋值直接使用，会报错
"""
i = 123
f = 123.456
s = '   123'
b = True
n = None
print('type change:', float(s))

'''
# 列表和元组
- 可以放置任意数据类型的有序集合，支持索引取值（支持负索引）、切片
1. list
  - 可以随意地增加(append、extend、insert)、删(remove、pop、del)或者改变元素
  - 使用[]包裹元素
2. tuple
  - 不能增加、删减或者改变元素
  - 使用()包裹元素
'''
l = [1, 2, 3]
t = (4, [5, 6])
## 末尾添加，只接受一个元素
l.append(3)
## 将另外一个可迭代对象中所有元素添加到末尾
l.extend(t)
## 指定位置插入
l.insert(0, 10)
## 移除第一个值为指定值的项
l.remove(3)
## 移除并返回指定位置的元素，没有指定位置则默认为最后一位
l.pop(-2)
## 删除某一项或整个列表
del l[1]
print('l:', l)

'''
## 差异
1. 存储方式不同
  - 由于列表是动态的，需要额外存储其空间已经分配的大小，用于追踪空间使用程度，当空间不足时候能够及时分配新空间
  - 分配过程：每次分配或额外多分配一点
'''
print('list tuple diff:', [1, 2, 3].__sizeof__(), (1, 2, 3).__sizeof__())

''''
# 字典和集合
- 使用{}包裹元素，本质是哈希表
1. dict
  - 由一系列键值对配对组成的元素集合，3.7+被确认为有序的
2. set
  - 一系列无序、唯一的元素组成，不支持索引操作
'''
d = {'name':'xxy', 1: 2, 'age': 20}
d[1] = 1
d['name'] = 'xxyCoder'
## 添加元素
d['addr'] = 'China'
## 删除元素
del d['name']
d.pop(1)
## get(key, default)
print('dict get:', d.get('name', 'xxy'))

s = { 1, 2, 3, 3 }
## 添加一个或多个
s.add(5)
s.update([7, 8, 9, 9])
## 删除一个，remove对于不存在元素抛出错误，discard则不会抛出错误，pop随机移除一个元素，如果为空集合则报错
s.remove(1)
s.discard(0)
s.pop()
print('set dict:', s, d)

'''
# array.array
- 只能存储同一种数据类型的元素
'''
import array
a = array.array('i', [1, 2, 3])

# 通过type()告知变量类型
print('type:', type(i), type(f), type(s), type(b), type(n), type(l), type(t), type(d), type(a))