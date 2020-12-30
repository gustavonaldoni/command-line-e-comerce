from os import system, name
import time

def clean_terminal(time_to_clean_in_seconds):

    time.sleep(time_to_clean_in_seconds)
    
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')