import CoffeeData

c = CoffeeData

def espresso_maker():
    print("espresso made")


def reporter():
    print("Water:", c.resources["water"], "\nMilk: ", c.resources["milk"], "\nCoffee:", c.resources["coffee"])


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
        esp = c.MENU["espresso"]["cost"]
        if money_entered > esp:
            change = money_entered - esp
            print("your change is: ", change)
            espresso_maker()
        else:
            print("sorry, not enough money!")
            selector()


selector()
