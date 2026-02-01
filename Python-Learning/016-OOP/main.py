from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    # 1 prompt user
    user_input = input("What would you like? (espresso/latte/cappuccino)")

    # 2 turn off user_input machine
    if user_input == "off":
        return
    
    # 3 Show report 
    if user_input == "report":
        return


if __name__ == "__main__":
    main()
