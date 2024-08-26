import re


def user_name():
    """
    Prompts the user to enter a valid username. The username must be between 2 and 11 characters long,
    starting with a non-whitespace character. It can contain alphanumeric characters and underscores.

    """
    pattern = r"^\S\w{1,10}$"

    while True:
        username = input("Type your username: ")
        result = re.search(pattern, username)

        if result:
            print("Username is valid")
            return username
        else:
            print("Invalid username. Please enter a valid username and try again.")
