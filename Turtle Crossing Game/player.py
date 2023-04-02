from time import *
from turtle import *
from cars import *
from scoreboard import *

dist = 20


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -270)
        self.setheading(90)
        self.showturtle()

    def move_turtle(self):
        self.forward(20)

    def detect_collision(self):
        for i in cars:
            if self.distance(i) < dist:
                self.hideturtle()
                Scoreboard.game_over(self)
                sleep(2)
                game_on = False
                break
            else:
                game_on = True
        return game_on

    def level_up(self):
        global dist
        dist += 10
