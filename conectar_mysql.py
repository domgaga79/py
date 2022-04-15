import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost";
    user= "root";
    password= "";
    database= "bd_python"
)


print (mydb)

#mydb = mysql.execute("SELECT * FROM admin")

#for x in rows(mydb):
#    print(x)
