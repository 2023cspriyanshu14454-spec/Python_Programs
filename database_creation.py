import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydb6")
if mycursor:
    print(mydb.get_server_info())
    print("database created successfully")
