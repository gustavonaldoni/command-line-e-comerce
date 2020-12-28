from database.connection import MySQLConnector


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
        query = 'SELECT * FROM products'

        self.mycursor.execute(query)

        result = self.mycursor.fetchall()

        return result

class AccountHandler(MySQLConnector):
  
    def save_user_on_database(self,first_name,last_name,email, password):
        query = 'INSERT INTO users(first_name,last_name,email,password) VALUES(%s,%s,%s,%s)'
        values = (first_name, last_name, email, password)

        self.mycursor.execute(query, values)
        self.mydb.commit()