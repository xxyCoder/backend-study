'''
# 插入数据
ins1 = insert(table_name).values(column1="", column2="", ...)
ins2 = insert(table_name).values([
  { column1="", column2="" },
  ...
])
ins3 = insert(table_name).from_select([column1, column2, ...], select_stmt)
'''

'''
# 更新数据
upt = update(table_name)
      .where(table_name.column = opt)
      .values(column="")
'''

'''
# 删除数据
del = delete(table_name)
      .where(table_name.column = opt)
'''