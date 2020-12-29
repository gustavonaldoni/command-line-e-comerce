def show_welcome_message(store_name):
    print()
    print(f'==== Welcome to {store_name} ====')

def show_welcome_options():
    print()
    print("""-- Main Menu --

[1] Register
[2] Login
[3] Exit program""")

def ask_user_for_welcome_option():
    print()
    user_choice = int(input('Your choice: '))

    return user_choice