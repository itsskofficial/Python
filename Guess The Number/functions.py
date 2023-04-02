# includes all the functions required for main

from random import *


def guess():
    num = randint(1, 100)
    return num


def game(num, difficulty):
    if difficulty == "Easy":
        lives = 10
    elif difficulty == "Hard":
        lives = 5
    user_guess = 0
    print("\nI am thinking of a number from 1 to 100")
    while lives > 0 and user_guess != num:
        user_guess = int(input("Can you guess it? "))
        if user_guess >= num + 10:
            print("\nToo high!\nTry again")
        elif user_guess <= num + 10 and user_guess > num:
            print("\nA little high!\nTry again")
        elif user_guess <= num - 10:
            print("\nToo low!\nTry again")
        elif user_guess >= num - 10 and user_guess < num:
            print("\nA little low!\nTry again")
        if user_guess != num:
            lives -= 1
            print("\nLives remaining: %d\n" % lives)

    if user_guess == num:
        print("You guessed it right!")
    else:
        print("You ran out of lives!\nThe number was %d" % num)
