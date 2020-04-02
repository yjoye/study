import pymysql

db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()

with open('image.jpg','rb') as f:
    date = f.read()
try:
    sql = "update class set image = %s where name = 'Emma';"
    cur.execute(sql,[date])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

# 关闭数据库
cur.close()
db.close()