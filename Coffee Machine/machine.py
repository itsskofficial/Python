from machine import *
from art import *
from data import *
from os import *


def transaction(quarters, dimes, nickels, pennies, cost, coffee):
    money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.05
    if money == cost:
        resources["money"] += money
        make_coffee(coffee, cost)
    elif money < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = money - cost
        print("Here is your change of %.2f" % change)
        make_coffee(coffee, cost)


def make_coffee(coffee, cost):
    for key, value in MENU[coffee]["ingredients"].items():
        resources[key] -= value
    print("\nHere is your %s. Enjoy!" % coffee.title())


def check_resources(coffee):
    i = 0
    check = 0
    for key, value in MENU[coffee]["ingredients"].items():
        i += 1
        if value <= resources[key]:
            check += 1
        else:
            print("Sorry, there is not enough %s to make %s" % (key, coffee))
    if check == i:
        if coffee == "espresso":
            print("Okay, an %s costs $ %.2f" % (coffee, MENU[coffee]["cost"]))
        else:
            print("Okay, a %s costs $ %.2f" % (coffee, MENU[coffee]["cost"]))
        quarters = int(input("\nHow many quarters? "))
        dimes = int(input("\nHow many dimes? "))
        nickels = int(input("\nHow many nickels? "))
        pennies = int(input("\nHow many pennies? "))
        transaction(quarters, dimes, nickels, pennies, MENU[coffee]["cost"], coffee)
    else:
        restart()


def command(user_command):
    if user_command == "off":
        print("\nSwitching off")
        system("exit")
    elif user_command == "report":
        for key, value in resources.items():
            print(f"\n{key.title()} : {value}")
    elif (
        user_command == "espresso"
        or user_command == "latte"
        or user_command == "cappuccino"
    ):
        check_resources(user_command)
    else:
        print("Please type a valid button")
        restart()


def restart():
    print(logo)
    user_command = input("Espresso, Latte or Cappuccino\nWhat would you like? ")
    command(user_command.lower())
