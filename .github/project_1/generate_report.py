
import time

def generate_report(username, purchases):
    if not purchases:
        print("Please enter at least one purchase before generating a report.")
        return

    print("\nGenerating report... [**bonus**: You can sleep for 2 seconds]")
    time.sleep(2)

    total_delivery_charges = len(purchases) * 2.5 

    total_item_cost = 0
    most_expensive = None
    least_expensive = None

    for purchase in purchases:
        total_item_cost += purchase["total_cost"]

        if purchase["total_cost"] > most_expensive["total_cost"]:
            most_expensive = purchase

        if purchase["total_cost"] < least_expensive["total_cost"]:
            least_expensive = purchase

    average_cost = total_item_cost / len(purchases)

    print("                 -------------------------")
    print("                 | Amazon Expense Report |")
    print("                 -------------------------")
    print(f"name: {username}    password: {'*' * len(registered_users[username])}      Tel: +49***20      Date: {time.strftime('%m/%d/%Y')}")
    print("----------------------------------")
    print(f"DELIVERY CHARGES       TOTAL ITEM COST")
    print(f"  {total_delivery_charges} EURO                 {total_item_cost} EURO\n")
    print(f"MOST EXPENSIVE        LEAST EXPENSIVE")
    print(f"name: {most_expensive['item']}            name: {least_expensive['item']}")
    print(f"cost: {most_expensive['total_cost']} EURO          cost: {least_expensive['total_cost']} EURO\n")
    print(f"AVERAGE COST OF ITEM PER ORDER: {average_cost} EURO")
    print(f"PURCHASE DATE RANGE: {min(p['date'] for p in purchases)} to {max(p['date'] for p in purchases)}")
    print("--------")

    spending_limit = 500
    if total_item_cost > spending_limit:
        print("Note: You have exceeded the spending limit of", spending_limit, "EURO")
    else:
        print("Note: You have not exceeded the spending limit of", spending_limit, "EURO")
