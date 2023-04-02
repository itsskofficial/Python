from turtle import *
from random import *

COLORS = ["red", "blue", "green", "yellow", "orange"]
START_POS_Y = []
for i in range(-240, 240, 20):
    START_POS_Y.append(i)
cars = []
spd = 20


class Cars(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.shape("square")
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.penup()
        self.goto(300, choice(START_POS_Y))
        self.setheading(180)
        self.showturtle()
        self.speed(10)
        global cars
        cars.append(self)

    def move_cars(self):
        for i in cars:
            i.forward(spd)

    def increase_speed(self):
        global spd
        spd += 10
