MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    for key, value in resources.items():
        if key == "water" or key == "milk":
            print(f"{key.title()}: {value}ml")
        elif key == "coffee":
            print(f"{key.title()}: {value}g")
        elif key in resources and key == "money":
            print(f"{key.title()}: ${value}")

def check_resources(order, resource):
    for key, value in MENU[order]["ingredients"].items():
        if value > resource[key]:
            return f"Sorry, there is not enough {key}."
        elif order not in MENU:
            return False
        return True

def insert_coins(enough_ingredients):
    total_money = 0
    if enough_ingredients:
        quarters = int(input("How many quarters($0.25)?: "))
        dimes = int(input("How many dimes($0.10)?: "))
        nickles = int(input("How many nickles($0.05)?: "))
        pennies = int(input("How many pennies($0.01)?: "))
        total_quarters = 0.25 * quarters
        total_dimes = 0.10 * dimes
        total_nickles = 0.05 * nickles
        total_pennies = 0.01 * pennies
        total_money = round((total_pennies + total_dimes + total_nickles + total_quarters), 2)
    return total_money

def check_coins_against_price(order, coins):
    espresso_price = MENU['espresso']['cost']
    latte_price = MENU['latte']['cost']
    cappuccino_price = MENU['cappuccino']['cost']
    if order == "espresso" and coins > espresso_price:
        print(f"Here is ${round(coins - espresso_price, 2)} dollars in change.")
        return True
    elif order == "latte" and coins > latte_price:
        print(f"Here is ${round(coins - latte_price, 2)} dollars in change.")
        return True
    elif order == "cappuccino" and coins > cappuccino_price:
        print(f"Here is ${round(coins - cappuccino_price, 2)} dollars in change.")
        return True
    else:
        return False

def adjust_resources(order, resources):
    resources['water'] -= MENU[order]["ingredients"]["water"]
    resources['milk'] -= MENU[order]["ingredients"]["milk"]
    resources['coffee'] -= MENU[order]["ingredients"]["coffee"]
    return resources

def make_coffee():
    is_on = True
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            is_on = False

        elif user_choice == "report":
            report()
            make_coffee()
        elif user_choice not in MENU:
            print("Please select valid menu from the list above")
        else:
            enough_ingredients = check_resources(user_choice, resources)
            print("Please insert coins.")
            funds = insert_coins(enough_ingredients)
            print(f"You've inserted ${funds} in total.")

            resources["money"] = funds

            enough_funds = check_coins_against_price(user_choice, funds)
            print(enough_funds)
            adjust_resources(user_choice, resources)
            if enough_funds:
                report()
                print(f"Here is your {user_choice}. ☕ ☕ ☕ Please enjoy!")
                is_on = False
            else:
                print(f"Sorry that's not enough money. Money refunded.")


make_coffee()