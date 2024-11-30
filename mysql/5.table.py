from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, PrimaryKeyConstraint, select
engine = create_engine('sqlite:///test.db', echo=True)
'''
# 创建表
create table table_name {...}

Table(table_name, metadata, Column(column_name, column_type), Column(), ...)
'''
metadata = MetaData()
users = Table("users", metadata,
              Column("id", Integer),
              Column("name", String),
              Column("age", String, default = 0)
              PrimaryKeyConstraint("id", "name")
            )
orders = Table("orders", metadata,
               Column('id', Integer, primary_key = True, autoincreament = True),
               Column('user_id', Integer, ForeignKey('users.id')),
              )

'''
# 修改表
alter table table_name [add|drop] column_name (type)

new_column = Column(column_name, type)
table_name.append_column(new_column)
metadata.create_all(engine)

## 更新列
table_name.c.column_name.type = new_type
metadata.create_all(engine)

table_name.columns.pop(column_name)
metadata.create_all(engine)
'''

'''
# 视图，虚拟的表。与包含数据的表不一样，视图只包含使用时动态检索数据的查询。
create view view_name
drop view view_name
create or replace view view_name

## 查看视图语句
show create view view_name
'''
users_view = select([users]).alias("users_view")
metadata.create_all(engine, tables=[users_view])