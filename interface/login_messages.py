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

def show_success_login_message(user_first_name, user_last_name):
    full_name = f'{user_first_name} {user_last_name}'

    print()
    print(f'Hi, {full_name}! You are logged in.')