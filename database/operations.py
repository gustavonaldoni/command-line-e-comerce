from database.connection import MySQLConnector
import bcrypt


class PromotionalCodeOperator(MySQLConnector):

    def save_code_on_database(self, promotional_code):
        code = promotional_code.code
        discount_percentage = promotional_code.discount_percentage

        query = 'INSERT INTO promotional_codes(code, discount_percentage) VALUES(%s, %s)'
        values = (code, discount_percentage)

        self.mycursor.execute(query, values)
        self.mydb.commit()


class ProductOperator(MySQLConnector):

    def save_product_on_database(self, product):
        name = product.name
        price = product.price

        query = 'INSERT INTO products(name, price) VALUES(%s, %s)'
        values = (name, price)

        self.mycursor.execute(query, values)
        self.mydb.commit()

    def select_all_products_from_database(self):
        query = 'SELECT name, price FROM products'

        self.mycursor.execute(query)

        result = self.mycursor.fetchall()

        return result

class AccountHandler(MySQLConnector):
  
    def save_user_on_database(self, first_name, last_name, email, password, salt):
        query = 'INSERT INTO users(first_name,last_name,email,password, salt) VALUES(%s,%s,%s,%s,%s)'
        values = (first_name, last_name, email, password, salt)

        self.mycursor.execute(query, values)
        self.mydb.commit()

    def select_all_user_information(self, user_id):
        query = 'SELECT * FROM users WHERE id = %s'
        values = (user_id, )

        self.mycursor.execute(query, values)

        result = self.mycursor.fetchall()

        return result

class RegisterOperator(AccountHandler):

    def register_user_on_database(self, first_name, last_name, email, password):
        first_name = first_name.title()
        last_name = last_name.title()

        password = password.encode()
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password, salt)

        self.save_user_on_database(first_name, last_name, email, hashed_password, salt)

class LoginOperator(MySQLConnector):
    pass