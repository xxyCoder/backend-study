'''
# 子查询，嵌套在其他查询中的查询
- 在SELECT语句中，子查询总是从内向外处理
select column1, (select column1 from table_name3 where table_name1.column2 = table_name3.column1) as alias_name from table_name1
where column2 in (
  select column1 from table_name2
)
- 从table_name1表中查询column2在table_name2中的行数据，对于每一行都需要执行select中的子select查询
'''

'''
selectSubQuery = select(table_name1.column1).where(table_nam1.column2 = table_name2.column).lable("alias_name")
whereSubQuery = select(table_name2.column1).alias('whereSubQuery')
query = select(table_name3.column, selectSubQuery).where(table_name.column2.in_(whereSubQuery))
'''

'''
# 表联结
join_query = select(table_name1.column1, ...)
            .select_from(
              table_name1.join(table_name2, table_name1.column = table_name2.column)
            )

left_join_query = select(table_name1.column1, ...)
                  .select_from(
                    table_name1.outerjoin(table_name2, table_name1.column = table_name2.column)
                  )

full_join_query = select(table_name1.column1, ...)
                  .select_from(
                    full_join(table_name1, table_name2, table_name1.column = table_name2.column)
                  )
'''

'''
# union查询
- UNION中的每个查询必须包含相同的列、表达式或聚集函数（不过各个列不需要以相同的次序列出）​
- UNION从查询结果集中自动去除了重复的行，可以使用union all代替，从而取消

query1 = select(...)
query2 = select(...)
union_query = union(query1, query2)
union_all_query = union_all(query1, query2)
'''
