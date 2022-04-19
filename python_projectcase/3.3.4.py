import sqlite3

con = sqlite3.connect("sales.db")
cur = con.cursor()
cur.execute("select id,price,name from book")
for row in cur:
    print(row)
