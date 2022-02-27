import pymysql

# 连接MySQL
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', charset='utf8')
cursor = conn.cursor()
# 1.查看数据库
# 发送指令
cursor.execute("show databases")
# 获取结果
result = cursor.fetchall()
print(result)

# 2.创建数据库
cursor.execute("create database mydb default charset utf8 collate utf8_general_ci")
conn.commit()
#
cursor.execute("show databases")
result = cursor.fetchall()
print(result)
# 进入数据库查看表
cursor.execute("use mysql")
cursor.execute("show tables")
result = cursor.fetchall()
print(result)

# 4.删除数据库
cursor.execute("drop database mydb")
conn.commit()
#
cursor.execute("show databases")
result = cursor.fetchall()
print(result)
# 关闭连接
cursor.close()
conn.close()
