from data import *
from art import *
from random import *
from os import *


def game():
    temp_data = data
    score = 0
    a = choice(temp_data)
    temp_data.remove(a)
    print(f"\nCompare A: {a['name']} a {a['description']} from {a['country']}")
    b = choice(temp_data)
    temp_data.remove(b)
    print("\n%s\n" % vs)
    print(f"Compare B: {b['name']} a {b['description']} from {b['country']}")
    answer = input("\nWho has more followers? ")
    if answer == "A":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            game2(a, temp_data, score)
        else:
            print("\nThat's not right")
            print("Final score: %d" % score)
    elif answer == "B":
        if a["follower_count"] < b["follower_count"]:
            score += 1
            game2(b, temp_data, score)
        else:
            print("\nThat's not right")
            print("Final score: %d" % score)


def game2(a, data, score):
    b = choice(data)
    data.remove(b)
    print(logo)
    system("cls")
    print("\nYou got it! Current score: %d" % score)
    print(f"\nCompare A: {a['name']} a {a['description']} from {a['country']}")
    print("\n%s\n" % vs)
    print(f"Compare B: {b['name']} a {b['description']} from {b['country']}")
    answer = input("\nWho has more followers? ")
    if answer == "A":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            game2(a, data, score)
        else:
            print("\nThat's not right")
            print("Final score: %d" % score)
    elif answer == "B":
        if a["follower_count"] < b["follower_count"]:
            score += 1
            game2(b, data, score)
        else:
            print("\nThat's not right")
            print("Final score: %d" % score)
