import re
import time


def login(attempts, registered_users):
    attempts = 3
    # registered_users = {}

    for x in range(attempts):
        #print(x)
        username = input("Enter username : ")
        password = input("Enter password :")

        if username in registered_users and registered_users[username]['password'] == password:
            print(" Login is successful")
            return username
        else:
            print("Invalid username or password. Please try again.")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

    print("You have used all login attempts. Try again after 5 seconds.")
    time.sleep(5)
    return None  # login(attempts, registered_users)
