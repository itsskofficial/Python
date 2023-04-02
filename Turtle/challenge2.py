# draw a dashed line
from turtle import *

t = Turtle()
t.color("black")


def dashed_line():
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


for i in range(10):
    dashed_line()

screen = Screen()
screen.exitonclick()
