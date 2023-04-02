# Draw a square

from turtle import *

t = Turtle("turtle")
t.color("red")


def square():
    for i in range(4):
        t.forward(100)
        t.left(90)


square()
screen = Screen()
screen.exitonclick()
