import mysql.connector

conn = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='meioambiente')

cursor = conn.cursor()

cursor.execute("""INSERT INTO messages(Text, Date,Users_UserId) VALUES ('OI', '2022-10-21 00:00:00', 1)""")

#cursor.execute("""INSERT INTO users(Username, Password) VALUES ('biruleibe', '1234')""")

conn.commit()

#Closing the connection
conn.close()