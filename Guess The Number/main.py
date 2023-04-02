# just runs the program

from art import *
from random import *
from functions import *

play_game = True

while play_game:
    print(logo)
    print("Welcome to Guess The Number!")
    difficulty = input("Choose your difficulty, Easy or Hard? ")
    num = guess()
    game(num, difficulty)
    play_game = bool(int(input("\nType 1 if you want to play again or 0 to quit: ")))
