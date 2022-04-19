import sqlite3

books = [("021", 25, "大学计算机"), ("022", 30, "大学英语"), ("023", 18, "艺术欣赏"), ("024", 35, "高级程序语言设计")]
# 打开数据库
con = sqlite3.connect("sales.db")
# 创建游标对象
cur = con.cursor()
# 插入一行对象
cur.execute("insert into book(id,price,name) values('001',33,'大学计算机多媒体')")
cur.execute("insert into book(id,price,name) values(?,?,?) ", ("002", 28, "数据库基础"))
# 插入多行数据
cur.executemany("insert into book(id,price,name) values (?,?,?) ", books)
# 修改一行数据
cur.execute("Update book set price=? where name=?", (25, "大学英语"))
# 删除一行数据
n = cur.execute("delete from book where price=?", (25,))
print("删除了", n.rowcount, "行数据")
con.commit()
cur.close()
con.close()
