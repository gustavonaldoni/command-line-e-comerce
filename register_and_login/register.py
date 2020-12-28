import bcrypt
from database.operations import AccountHandler


def register_user_on_database(first_name, last_name, email, password):
    handler = AccountHandler()

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    handler.save_user_on_database(first_name, last_name, email, hashed_password)
