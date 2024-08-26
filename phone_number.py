import re


def phone_number():
    """
    Prompts the user to input a valid German phone number. The phone number must start with '+49'
    followed by 1 to 10 digits.
    """
    check = r'^(\+49)\d{1,10}$'

    while True:
        phonenumber = input("Write a valid German phone number: ")
        result = re.match(check, phonenumber)

        if result:
            anonymos = phonenumber[:-4] + "****"
            print("Valid phone number! ", anonymos)
            return phonenumber
        else:
            print("Invalid phone number. Please enter a valid German phone number.")
            print('Should start with "+49" followed by 1 to 10 digits.')

