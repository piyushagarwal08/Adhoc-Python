#!/usr/bin/python
import mysql.connector as mysql

# RDS information
username='enter-username'
password='enter-your-pass'
database_name='enter-db-name'
host='enter-end-point-of-db'

# Now connecting the Database
conn=mysql.connect(user=username,password=password,database=database_name,host=host)

# Now generating a SQL language cursor 
cur = conn.cursor()

# Now we can write SQL query
#cur.execute('show tables;')

# Now printing data
#print(cur.fetchall())

# closing connection
#conn.close()
