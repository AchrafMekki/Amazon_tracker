import re
import time


def enter_purchase(username, purchases):
    date = input("Enter the date of the purchase (MM/DD/YYYY or MM-DD-YYYY): ")
    item = input("Enter the item purchased (at least 3 characters): ")

    while len(item) < 3:
        print("Item name should be at least 3 characters. Please enter a valid item name.")
        item = input("Enter the item purchased (at least 3 characters): ")

    while True:
        try:
            total_cost = float(input("Enter the total cost of the item (including charges on delivery): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the total cost.")

    while True:
        try:
            weight = float(input("Enter the weight of the item (in kg): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the weight.")

    while True:
        try:
            quantity = int(input("Enter the quantity purchased (1 and above): "))
            if quantity < 1:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer value for the quantity (1 and above).")
    purchase = {
        "date": date,
        "item": item,
        "total_cost": total_cost,
        "weight": weight,
        "quantity": quantity,
    }

    purchases.append(purchase)
    print("Purchase recorded successfully!")