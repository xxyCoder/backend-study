'''
# 表
- show tables;
- show columns from table_name;
'''

'''
# 检索数据 
select [distinct] column_name1, column_name2, ..., column_namen 
from table_name 
where column_name [NOT] [= | != | between...and | in | is null | like | regexp] [AND | OR]
group by column_name having ...
order by column_name1 [sort:ASE|DESC=ASE], column_name2 [sort:ASE|DESC=ASE], ...
limit [offset_cnt=0, ]line_cnt;
- distinct必须在所有列前，因为其功能是应用所有列
- where在匹配的时候默认不区分大小写，in比or执行清单更快
- select中的列名必须在group by中给出，having对分组进行过滤
- ASE和DESC只应用于其前面的列名
'''
from sqlalchemy import select
'''
# query = select(table_name | table_name.column | table_name.column.label('alias'))
        .where(
          table_name.column_name1 judge condition,
          ~table_name.column_name2 judge condition,
          ...,
          and_(
            or_(table_name.column3 judge condition, table_name.column4 judge condition),
            table_name.column5 judge condition,
            table_name.column6.value.in_([condition1, ...])
          ),
          table_name.column7.like('condition'),
          table_name.column8.op('regexp')('condition'),
        )
        .group_by(table_name.column)
        .having(...)
        .order_by(
          table_name.column,
          table_name.column.desc()
        )
        .offset()
        .limit()
- from子句将自动推断为所有的Table对象 => from table1, table2, ...
- where中逗号使用or_连接（除了and_语句内），~表示not操作
'''