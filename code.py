#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "test", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
sql="select * from comment where name='su' and date='2019-11-07'"
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("data : %s " % str(data))

# 关闭数据库连接
db.close()