# 内置类型

## 容器序列
- list、tuple、collections.deque
1. 存放的是所包含任何类型的引用

## 扁平序列
- str、bytes、array.array
1. 存放的是所包含任何类型的值

## py对象结构
- ob_refcnt：对象引用次数
- ob_type：指向对象类型的指针
- ob_val：对象值
  - float: ob_fval