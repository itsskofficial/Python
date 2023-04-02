from turtle import *
from random import *

red = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
red.color("red")
green.color("green")
blue.color("blue")
turtles = {red, green, blue}
is_race_on = False
s = Screen()
s.setup(width=500, height=500)
play_again = "Yes"
while play_again == "Yes":
    user_guess = s.textinput(
        title="Make your bet!",
        prompt="Which turtle will win the race?\nRed, Blue or Green?",
    )
    if user_guess:
        is_race_on = True
    red.penup()
    green.penup()
    blue.penup()
    red.goto(x=-190, y=30)
    blue.goto(x=-190, y=0)
    green.goto(x=-190, y=-30)
    winner = ""

    while is_race_on == True:
        for i in turtles:
            i.forward(randint(1, 10))
            print
            if i.xcor() >= 190:
                winner = i.color()
                is_race_on = False
                break
            else:
                continue
    if user_guess == winner[0].title():
        play_again = textinput(
            title="You win!",
            prompt="%s has won the race! Do you want to play again?"
            % winner[0].title(),
        )
    else:
        play_again = textinput(
            title="You lose!",
            prompt="%s has won the race! Do you want to play again?"
            % winner[0].title(),
        )

s.bye()
