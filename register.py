import re
import time


def register(username, password, phone, registered_users):
    if username in registered_users:
        print("Username already exists. Please choose another one.")
        return False
    else:
        registered_users[username] = {'password': password, 'phone': phone}
        print(f"{username} You have successfully registered!")
        print("Updated registered_users:", registered_users)
        return True
