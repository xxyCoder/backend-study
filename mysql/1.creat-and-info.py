'''
# 连接数据库
1. 主机名，本地为localhost
2. 端口，默认3306
3. 用户名
4. 密码

# 选择数据库
- use databse_name;
- show databases;
'''
from sqlalchemy import create_engine
'''
# engine = create_engine('sqlite://user:password@hostname/database', echo=True)
  - sqlite表明和什么数据库连接
  - echo表示将所有SQL日志记录到一个py日志记录器，该记录器写入标准输出
engine是数据库引擎，对连接的抽象表示，隐藏不同数据库的操作差异；其内部管理一个连接池，当与数据库交互时，engine从连接池取出可用连接
'''
engine = create_engine('mysql://root:123456@localhost/py_db')
conn = engine.connect()