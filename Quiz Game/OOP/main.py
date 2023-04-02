from question_model import *
from data import *
from quiz_brain import *
from art import *


i = 0
game_play = "Yes"
while game_play == "Yes":
    print(logo)
    print("Welcome to Quiz Game!\n")
    question_bank = []

    for item in question_data[i]:
        ques = item["text"]
        ans = item["answer"]
        question = Question(ques, ans)
        question_bank.append(question)
        quiz = Quiz(question_bank)

    while quiz.question_remaining() == True:
        quiz.ask_question()

    print(
        "\nThanks for playing quiz game!\nYour final score is %d out of %d"
        % (quiz.points, len(question_bank)),
    )

    game_play = input("\nDo you want to play again? ")
    i += 1
