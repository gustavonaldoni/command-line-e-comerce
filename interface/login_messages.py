def ask_user_to_login():
    print()
    print('--- LOGIN PROCESS ---')
    print()

    user_email = input('Your email: ')
    user_password = input('Your password: ')

    return (user_email, user_password)

def show_invalid_email_message(user_email):
    print()
    print(f'Your email "{user_email}" does not exist.')