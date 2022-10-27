import mysql.connector

class DbConnector:

    user = "root"
    password = "1234"
    host = "127.0.0.1"
    database = "meioambiente"

    def __init__(self):
        self.conn = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        pass

    def createMessage(self, text, user, date):
        cursor = self.conn.cursor()
        cursor.execute(f"""INSERT INTO messages(Text, Date,Users_UserId) VALUES ('{text}', '{date}', '{user}')""")
        self.conn.commit()

    def searchUser(self, username):
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT * FROM users WHERE users.username = '{username}'""")
        result = cursor.fetchone()
        return result
        

    def closeConnection(self):
        self.conn.close()

    
if __name__ == "__main__":
    conn = DbConnector()
    conn.searchUser('a','')
    conn.closeConnection()
