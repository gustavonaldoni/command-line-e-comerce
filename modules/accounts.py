import bcrypt

from database.operations import AccountHandler


def register(first_name,last_name,email, password):
    handler = AccountHandler()
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    handler.add_user(first_name,last_name,email,password_hash)
