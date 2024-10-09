import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="PET"
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM store")
print(mycursor.fetchall())


