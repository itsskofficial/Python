from turtle import *
from snake import *
from random import *


class Food:
    def __init__(self) -> None:
        self.food = Turtle(shape="circle")
        self.food.speed(0)
        self.food.color("red")
        self.food.penup()
        self.food.shapesize(0.7, 0.7)
        self.x = randint(-200, 200)
        self.y = randint(-200, 200)
        self.food.goto(self.x, self.y)

    def refresh(self):
        self.x = randint(-200, 200)
        self.y = randint(-200, 200)
        self.food.goto(self.x, self.y)
