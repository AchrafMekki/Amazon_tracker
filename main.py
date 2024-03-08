import re
import time


from user_name import user_name
from password_validation import password_validation
from phone_number import phone_number
from register import register
from login import login
from enter_purchase import enter_purchase
from generate_report import generate_report




def main():
    print('\n\n#### Welcome to our new Amazon Tracker #####\n\n')
    print('******* Choose to Sign-in or to Register ********\n\n')

    step = input("---> Enter '1' to Register  OR  Enter '0' to Login: ")

    registered_users = {}
    purchases = []

    if step == '1':
        username =user_name()
        password =password_validation()
        phone = phone_number()
        register(username,password,phone,registered_users)


    elif step == '0':
        username = login(3, registered_users)
        if username:
            print("Welcome back,", username)
            while True:
                print("\nMenu:")
                print("1. Enter a purchase")
                print("2. Generate a report")
                print("3. Quit")

                choice = input("Select an option (1, 2, or 3): ")

                if choice == "1":
                    enter_purchase(username, purchases)
                elif choice == "2":
                    generate_report(username, purchases)
                elif choice == "3":
                    print(f"\nGoodbye, {username}! Thank you for using Amazon Expense Tracker.")
                    break
                else:
                    print("Invalid operation. Please select from the available options.")

    else:
        print("Invalid input.")


main()