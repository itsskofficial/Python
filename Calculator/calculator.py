from art import *
from data import *
from os import *


def calculator(choice):

    while choice != 3:
        if choice == 2:
            system("cls")
            print(logo)
            print("\nWelcome to the Pythonist Calculator!")
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
            print("\n")
        elif choice == 1:
            n1 = answer
            n2 = float(input("\nEnter the next number: "))
            print("\n")
        for key, item in operations.items():
            print(key, " ")
        operation = input("\n\nWhat operation do you want to perform? ")
        for key, item in operations.items():
            if key == operation:
                answer = item(n1, n2)
        print(f"\n{n1} {operation} {n2} = {answer}")
        print("\n1.Continue this operation\n2.Start a new operation\n3.Exit")
        choice = int(
            input("\nPlease select a option from above(enter the option no): ")
        )

    print("\nThankyou for using the Pythonist Calculator!")
