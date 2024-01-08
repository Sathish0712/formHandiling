#!C:/python/python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Welcome To My Page</h1>")

Form=cgi.FieldStorage()
FName=Form.getvalue("Name")
FAge=Form.getvalue("Age")
FMovie=Form.getvalue("Movie")
FSongs=Form.getvalue("Songs")
FSalary=Form.getvalue("Salary")
print("Thank You for visiting my page")
#print("<h1>",FName,FAge,FMovie,FSongs,FSalary,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Actor"
    )

mycursor=mydb.cursor()
sql="INSERT INTO fan(Name,Age,Movie,Songs,Salary)VALUES(%s,%s,%s,%s,%s)"
val=(FName,FAge,FMovie,FSongs,FSalary)
mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")

