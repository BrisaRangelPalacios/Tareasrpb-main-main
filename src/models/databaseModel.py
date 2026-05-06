import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="sige"  
        )

    def get_connection(self):
        return self.connection