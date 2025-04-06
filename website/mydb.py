import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yecgaa$*7'
)

cursorobject = dataBase.cursor()

cursorobject.execute("CREATE DATABASE elderco")
print("All Done!")