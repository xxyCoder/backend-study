# 选择数据库
use database_name;
- 必须先使用use打开数据库，才能读取数据

# 展示全部数据库
show databases;

# 展示数据库下全部表
show tables;

# 展示表中全部列
show columns from table_name

# 检索数据
1. select column_name from table_name，从table_name中检索所有column_name的值
2. select * from table_name，从table_name中检索所有列的值
3. select distinct column_name from table_name，从table_name中检索所有column_name的值并去重
4. select column_name from table_name limit size，从table_name中检索所有column_name的值并限制返回数量为size条
5. select column_name from table_name limit offset, size，从table_name中检索所有column_name的值并限制从offset位置返回数量为size条

# 排序
- 默认以底层表中出现的顺序显示
select column_name from table_name order by column_name DESC, column_name ASC

# 过滤
- 位于order by 之前
select column_name from table_name where condition
- AND OR IN() NOT LIKE %表示字符出现任意次数 _匹配单个字符

# 正则
select * from table_name where column_name regexp condition

# 计算字段
- 使用 + - * /
select column_name + column_name as alias_name from table_name

# 拼接字段
- Concat连接字段、RTrim去掉右边空格、LTrim()、Trim()
select Concat(Trim(column_name), '(', column_name ,')') as alias_name from table_name

# 日期函数
- CurDate() 返回当前日期
- CurTime() 返回当前时间
- Date()  返回日期时间的日期部分
- DateDiff()  计算两个日期之差
- Date_Format() 返回一个格式化的日期
- Day() 返回天数
- DayOfWeek() 返回星期几
- Hour()  返回小时
- Minute()  返回分
- Month() 返回月
- Second()
- Year()

# 汇聚函数
- avg()计算特定列值之和
- count()确定行的数目
- max()返回指定列的最大值
- min()返回指定列的最小值
- sum()返回指定列的和

# 分组
- group by分组，必须出现在where之后，order by之前
- having过滤分组

# 子查询
- 将一条select语句返回的结果用于另一条select语句的where子句
- 也可以在select语句中使用select语句

# 联结表

## 内部联结
select column_name from table_name_1, table_name_2 where table_name_1.key = table_name_2
select column_name from table_name_1 inner join table_name_2 on table_name_1.key = table_name_2.key

## 自联结
- 单条select中不止一次引用相同的表
select column_name from table_name where column_name in (select column_name from table_name where column_name='')
select t1.column_name, t2.column_name from table_column as t1, table_name as t2 where p1.key = p2.key

## 外部联结
- 许多联结将一个表中的行与另一个表中的行相关联。但有时候会需要包含没有关联行的那些行
select column_name from table_name left/right outer join table_name on table_name_1.key = table_name_2.key

# 组合查询
- 必须两个及以上的select，每个查询需要包含相同的列，order by只能使用在最后一条select语句，union自动去除重复的行，all返回所有
select column_name from table_name where column_name ...
union/all
select column_name from table_name where column_name ...