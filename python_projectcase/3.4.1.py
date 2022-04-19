# 导入SQLite驱动
import sqlite3

# 连接数据库，如果不存在，则新增
conn = sqlite3.connect("test2.db")
# 创建一个cursor
cursor = conn.cursor()
cursor.execute("drop table exam")
# 执行一条SQL语句，创建exam表
cursor.execute(
    "create table [exam]([question] varchar(80) null,[Answer_A] varchar(1) null,[Answer_B] varchar(1) null,"
    "[Answer_C] varchar(1) null,[Answer_D] varchar(1) null,[right_Answer] varchar(1) null)")
# 继续执行一条SQl语句，插入一条记录
cursor.execute(
    "insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,right_ANswer) values "
    "('哈雷彗星的平均周期为：','54年','56年','73年','83年','C')")
cursor.execute(
    "insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,right_ANswer) values "
    "('夜郎自大中“夜郎”指的是现在哪个地方：','贵州','云南','广西','福建','A')")
cursor.execute(
    "insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,right_ANswer) values "
    "('在中国历史上是谁发明了麻药：','孙思邈','华佗','张仲景','扁鹊','B')")
cursor.execute(
    "insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,right_ANswer) values "
    "('京剧中花旦是指：','年轻男子','年轻女子','年长男子','年长女子','B')")
cursor.execute(
    "insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,right_ANswer) values "
    "('篮球比赛每队几人？','4','5','6','7','B')")
cursor.execute(
    "insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,right_ANswer) values "
    "('在天愿作比翼鸟，在地愿为连理枝。讲述的是谁的爱情故事？','焦仲卿和刘兰芝','梁山伯和祝英台','崔莺莺与张生','杨贵妃与唐明皇','D')")
# 通过rowcount获得插入的行数
# cursor.execute("select count(*) from exam")
print(cursor.rowcount)
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭connection
conn.close()
