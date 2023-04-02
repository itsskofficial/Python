from machine import *
from art import *

print(logo)
user_command = input("Espresso, Latte or Cappuccino\nWhat would you like? ")
command(user_command.lower())
