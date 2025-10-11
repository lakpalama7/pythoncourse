
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="test")

mycursor=mydb.cursor()
mycursor.execute("select * from student")
allresult=mycursor.fetchall()



for i in allresult:
    print(i)

print("--"*10)

# oneresult=mycursor.fetchone()
# for i in oneresult:
#     print(i)