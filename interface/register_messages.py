def ask_user_for_register():
    print()
    print('--- REGISTRATION FORM ---')
    print()

    user_first_name = input('First Name: ')
    user_last_name = input('Last Name: ')
    user_email = input('Email: ')
    user_password = input('Password: ')

    return (user_first_name, user_last_name, user_email, user_password)

def show_success_registration_message():
    print()
    print('SUCCESS! - Your user account has been registered without errors.')

def show_invalid_email_message(user_email):
    print(f'Your email "{user_email}" is invalid.')

def show_invalid_password_message(user_password):
    print(f'Your password "{user_password}" is invalid.')

def show_error_registration_message():
    print()
    print('Oh no ... an error has occurred during your registration process')
    print('Please contact the support for more informations')