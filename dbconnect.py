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

with open('file.txt','r') as file:
    questions = file.readlines()
    for i in questions:
        question,option1,option2,option3,option4,answer = i.split('##')
        cur.execute('Insert into Docker_B(Question,Option1,Option2,Option3,Option4,Answer) values(questiton,option1,option2,option3,option4,answer);')

conn.close

# Now we can write SQL query
#cur.execute('show tables;')

# Now printing data
#print(cur.fetchall())

# closing connection
#conn.close()
