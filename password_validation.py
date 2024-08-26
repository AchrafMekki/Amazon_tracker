import re


def password_validation():
    """
    Prompts the user to enter a valid password. The password must contain:
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    - Be between 6 to 20 characters long
    """
    # Improved regex pattern
    pp = r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W).{6,20}$'

    while True:
        password = input("Write a valid password: ")
        result = re.search(pp, password)

        if result:
            print("Password is valid.")
            return password
        else:
            print("\nPlease enter a valid password:")
            print("1. Should have at least one number.")
            print("2. Should have at least one uppercase and one lowercase character.")
            print("3. Should have at least one special symbol.")
            print("4. Should be between 6 to 20 characters long.\n")

