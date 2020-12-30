from interface.initial_messages import show_welcome_message, show_welcome_options, ask_user_for_welcome_option
from interface.register_messages import ask_user_for_register, show_success_registration_message, show_invalid_email_message, show_invalid_password_message, show_error_registration_message
from interface.products_messages import show_all_products
from interface.terminal_cleaner import clean_terminal
from database.operations import RegisterOperator, AccountHandler
from validators.register import RegisterValidator

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
            pass
        elif user_option == 3:
            pass
       
main()
