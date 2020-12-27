import mysql.connector
import os

host = os.environ.get('ECOMMERCE_DB_HOST')
user = os.environ.get('ECOMMERCE_DB_USER')
password = os.environ.get('ECOMMERCE_DB_PASSWORD')
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
