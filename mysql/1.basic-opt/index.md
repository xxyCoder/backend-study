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