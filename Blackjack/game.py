# importing necessary files
from art import *
from random import *
from os import *


def Blackjack():
    game_choice = "Y"
    while game_choice == "Y":
        system("cls")
        cards1 = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        cards2 = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        user_cards = []
        user_score = 0
        computer_cards = []
        computer_score = 0
        chances = 0
        print(logo)
        print("\nWelcome to Blackjack!")
        for i in range(0, 2):
            card1 = choice(cards1)
            user_cards.append(card1)
            cards1.remove(card1)
        for i in user_cards:
            if i == "Ace":
                if (user_score + 11) > 21:
                    j = 1
                else:
                    j = 11
            elif i == "Jack" or i == "Queen" or i == "King":
                j = 10
            else:
                j = i
            user_score += j
        print(f"\nYour cards: {user_cards}\nYour score: {user_score}\n")
        card2 = choice(cards2)
        computer_cards.append(card2)
        cards2.remove(card2)
        for i in computer_cards:
            if i == "Ace":
                if (computer_score + 11) > 21:
                    j = 1
                else:
                    j = 11
            elif i == "Jack" or i == "Queen" or i == "King":
                j = 10
            else:
                j = i
            computer_score += j
        print(f"Computer's cards: {computer_cards}\nComputer score: {computer_score}\n")
        while user_score <= 21 and computer_score <= 21 and chances < 2:
            card_choice = input(
                "Please enter C to get another card or enter P to pass: "
            )
            if card_choice == "C":
                user_score = 0
                card1 = choice(cards1)
                user_cards.append(card1)
                cards1.remove(card1)
                for i in user_cards:
                    if i == "Ace":
                        if (user_score + 11) > 21:
                            j = 1
                        else:
                            j = 11
                    elif i == "Jack" or i == "Queen" or i == "King":
                        j = 10
                    else:
                        j = i
                    user_score += j
                print(f"\nYour cards: {user_cards}\nYour score: {user_score}\n")
                print(
                    f"Computer's cards: {computer_cards}\nComputer score: {computer_score}\n"
                )
            elif card_choice == "P":
                computer_score = 0
                card2 = choice(cards2)
                computer_cards.append(card2)
                cards2.remove(card2)
                for i in computer_cards:
                    if i == "Ace":
                        if (computer_score + 11) > 21:
                            j = 1
                        else:
                            j = 11
                    elif i == "Jack" or i == "Queen" or i == "King":
                        j = 10
                    else:
                        j = i
                    computer_score += j
                print(f"\nYour cards: {user_cards}\nYour score: {user_score}\n")
                print(
                    f"Computer's cards: {computer_cards}\nComputer score: {computer_score}\n"
                )
            chances += 1
        if user_score > 21:
            print("You went over. Computer wins!")
        elif computer_score > 21:
            print("Computer went over. You win!")
        elif chances == 2:
            if user_score > computer_score:
                print("You win!")
            elif user_score < computer_score:
                print("Computer wins!")
            else:
                print("Its a tie!")
        game_choice = input(
            "Please enter Y if you want to play again or enter N if you want to quit: "
        )
