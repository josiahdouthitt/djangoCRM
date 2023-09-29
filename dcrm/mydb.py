import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Soundboard490'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE recordways")

print("DATABASE CREATE COMPLETE")