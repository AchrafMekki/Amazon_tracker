import re
import time


def what_to_do_first(x):
    if x == "1":
        return "Here you can Register"
    elif x == "0":
        return "!!* Welcome Back *!!"
    else:
        return "Invalid input"


# Loop until a valid input is provided
while True:
    choose = input("---> Enter '1' to Register  --->  OR  --->  Enter '0' to Login: ")
    result = what_to_do_first(choose)
    print(result)

    if result != "Invalid input":
        break  # Exit the loop if the input is valid
