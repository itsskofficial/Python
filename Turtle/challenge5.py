# draw a spirograph
from turtle import *

t = Turtle()
t.color("black")
t.speed(0)


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        t.circle(100)
        t.setheading(t.heading() + gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
