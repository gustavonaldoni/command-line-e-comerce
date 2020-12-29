def ask_user_for_register():
    print()
    print('--- REGISTRATION FORM ---')
    print()

    user_first_name = input('First Name: ')
    user_last_name = input('Last Name: ')
    user_email = input('Email: ')
    user_password = input('Password: ')

    return (user_first_name, user_last_name, user_email, user_password)
