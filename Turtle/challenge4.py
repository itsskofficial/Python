# draw a random walk
from turtle import *
from random import *
import turtle

t = Turtle()
t.pensize(5)
turtle.colormode(255)
colors = ["violet", "indigo", "blue", "cyan", "green", "yellow", "orange", "red"]
directions = ["north", "east", "west", "south"]


def random_walk(line_color, direction):
    t.color(line_color)
    if direction == "north":
        t.forward(10)
    elif direction == "east":
        t.right(90)
        t.forward(10)
    elif direction == "west":
        t.left(90)
        t.forward(10)
    else:
        t.backward(10)


for i in range(1000):
    random_walk((randint(0, 255), randint(0, 255), randint(0, 255)), choice(directions))

screen = Screen()
screen.exitonclick()
