import mysql.connector
import os

host = os.environ.get('host','localhost')
user = os.environ.get('user')
password = os.environ.get('password')
database = 'ecommerce_db'

class MySQLConnector:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )

        self.mycursor = self.mydb.cursor()
