import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost";
    user= "root";
    password= "";
    database= "bd_python"
)

print (mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM admin")

for x in mycursor:
  print(x)
