import mysql.connector

class MySQLConnector:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='gugu0902',
            database='ecommerce_db'
        )

        self.mycursor = self.mydb.cursor()
