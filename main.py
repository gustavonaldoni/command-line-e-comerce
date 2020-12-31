from interface.initial_messages import show_welcome_message, show_welcome_options, ask_user_for_welcome_option
from interface.register_messages import ask_user_for_register, show_success_registration_message, show_invalid_email_message, show_invalid_password_message, show_error_registration_message
from interface.products_messages import show_all_products
from interface.terminal_cleaner import clean_terminal
from interface.login_messages import ask_user_to_login, show_invalid_email_message
from database.operations import RegisterOperator, AccountHandler, LoginOperator
from validators.register import RegisterValidator
from general_classes.user import User

def main():

    while True:

        show_welcome_message("Naldoni's")
        show_welcome_options()

        user_option = ask_user_for_welcome_option()

        if user_option == 1:
            clean_terminal(0.5)

            user_first_name, user_last_name, user_email, user_password = ask_user_for_register()

            register_validator = RegisterValidator()

            is_email_valid = register_validator.validate_email(user_email)
            is_password_valid = register_validator.validate_password(user_password)

            clean_terminal(0.5)
            if is_email_valid and is_password_valid:
                register_operator = RegisterOperator()

                try:
                    register_operator.register_user_on_database(user_first_name, user_last_name, user_email, user_password)
                    show_success_registration_message()
                except:
                    show_error_registration_message()
                    break
            
            print()

            if not is_email_valid:
                show_invalid_email_message(user_email)
            
            if not is_password_valid:
                show_invalid_password_message(user_password)

            clean_terminal(3)

        elif user_option == 2:
            clean_terminal(0.5)

            user_email, user_password = ask_user_to_login()

            login_operator = LoginOperator()

            does_email_exist = login_operator.check_if_email_exists(user_email)

            if not does_email_exist:
                show_invalid_email_message(user_email)
                
            else:
                user_id, hashed_password = login_operator.select_id_and_hashed_password_by_email(user_email)[0]
                
                is_password_valid = login_operator.check_password(user_password, hashed_password)

                if is_password_valid:
                    account_handler = AccountHandler()

                    all_account_information = account_handler.select_all_user_information(user_id)[0]

                    user_first_name = all_account_information[1]
                    user_last_name = all_account_information[2]
                    user_email = all_account_information[3]
                    user_creation_datetime = all_account_information[5]

                    user = User(user_id, user_first_name, user_last_name, user_email, user_creation_datetime)

                else:
                    print('INVALID PASSWORD')

            clean_terminal(3)

        elif user_option == 3:
            pass
       
main()
