# draw random shapes within shapes
from turtle import *

t = Turtle()
colors = ["violet", "indigo", "blue", "cyan", "green", "yellow", "orange", "red"]
angles = [120, 90, 72, 60, 51.43, 45, 40, 36]
sides = [3, 4, 5, 6, 7, 8, 9, 10]
side = 100


def draw_shapes(angle, no_of_sides, shape_color):
    t.color(shape_color)
    for i in range(no_of_sides):
        t.forward(side)
        t.left(angle)


for i in range(8):
    draw_shapes(angles[i], sides[i], colors[i])
# draw_shapes(120, 3, "red")

screen = Screen()
screen.exitonclick()
