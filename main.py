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
}

quarter = 0.25
penny = 0.01
nickle = 0.05
dime = 0.10


def espresso_maker():
    print("espresso made")

def reporter():
    print("Water:", resources["water"], "\nMilk: ", resources["milk"], "\nCoffee:", resources["coffee"])

def selector():
    reporter()
    selection = input("What would you like? (espresso/latte/cappuccino):")
    if selection == "off":
        exit()

    quarter_counter = int(input("How many quarters are you entering?"))
    dime_counter = int(input("How many dimes are you entering?"))
    nickle_counter = int(input("How many nickles are you entering?"))
    penny_counter = int(input("How many pennies are you entering?"))

    money_entered = quarter_counter * 0.25 + dime_counter * 0.10 + nickle_counter * 0.05 + penny_counter * 0.01

    if selection == "espresso":
        esp = MENU["espresso"]["cost"]
        if money_entered > esp:
            change = money_entered - esp
            print("your change is: ", change)
            espresso_maker()
        else:
            print("sorry, not enough money!")
            selector()


selector()
