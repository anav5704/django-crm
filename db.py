import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='godzilla',
    passwd='godzilla',
    port=3306
)

cursorObj = db.cursor()

cursorObj.execute("CREATE DATABASE customerdb")

print("db created")
