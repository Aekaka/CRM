import mysql.connector

dataBase = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd = '664209.Ab',

	)

#prepare a cursor object

cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE ArnoldCRM")

print("All Done")
