# 导入python SQLite数据库模块
import sqlite3

# 创建SQLite数据库
con = sqlite3.connect("sales.db")
# 创建表book,包含3列，即id(主键)、price和name
con.execute("create table book(id primary key,price,name)")
