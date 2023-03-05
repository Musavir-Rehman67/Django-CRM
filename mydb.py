import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = #username of mysql,
    passwd = #password Here,
)
# perpare a cursor object
cursorObject = dataBase.cursor()

# Create Database
cursorObject.execute("CREATE DATABASE myowncompany")

print("All Done!")