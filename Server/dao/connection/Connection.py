import mysql.connector
# from mysql.connector import Error

class Connection:
    def connect_mysql(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='music',
                username='root',
                password=''
            )
            cursor = self.connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            # print("You're connected to database: ", record)
            return self.connection
        except mysql.connector.Error as e:
            print("Error connecting to database:", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from database.")
