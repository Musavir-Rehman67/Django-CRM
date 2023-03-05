import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = 'Musavir@67'
)
# perpare a cursor object
cursorObject = dataBase.cursor()

# Create Database
cursorObject.execute("CREATE DATABASE myowncompany")

print("All Done!")