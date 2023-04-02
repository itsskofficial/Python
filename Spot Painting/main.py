import turtle
from colorgram import *
from turtle import *
from random import *


turtle.colormode(255)
colors = extract("image.jpg", 30)
turtle_colors = []
for i in colors:
    rgb_colors = (i.rgb.r, i.rgb.g, i.rgb.b)
    turtle_colors.append(rgb_colors)
turtle_colors = turtle_colors[4:]
t = Turtle()


def draw_painting(height, width, colors):
    facing = "east"
    while height > 0:
        for i in range(width):
            t.pendown()
            t.dot(15, choice(colors))
            t.penup()
            t.forward(30)
            t.pendown()
        if facing == "east":
            t.penup()
            t.left(90)
            t.forward(30)
            t.left(90)
            t.forward(30)
            facing = "west"
        elif facing == "west":
            t.penup()
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(30)
            facing = "east"
        height -= 1


draw_painting(10, 10, turtle_colors)

screen = Screen()
screen.exitonclick()
