import _mysql_connector
import mysql

mydb = mysql.connector.connect(

  host="localhost",

  user="yourusername",

  password=""
)

print(mydb)