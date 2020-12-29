from interface.initial_messages import show_welcome_message, show_welcome_options, ask_user_for_welcome_option
from interface.register_messages import ask_user_for_register
from interface.products_messages import show_all_products
from database.operations import RegisterOperator, AccountHandler

def main():

    show_welcome_message("Naldoni's")
    show_welcome_options()

    user_option = ask_user_for_welcome_option()

    if user_option == 1:
        user_first_name, user_last_name, user_email, user_password = ask_user_for_register()
    elif user_option == 2:
        pass
    elif user_option == 3:
        pass
       
main()
