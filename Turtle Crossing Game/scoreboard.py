from turtle import *
from cars import *


FONT = ("Times New Roman", 15, "bold")
level = 0


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.penup()
        self.color("black")

    def level(self):
        self.goto(-270, 270)
        self.write(f"Level:{level}", False, "left", FONT)

    def level_increase(self, player):
        global level
        if player.ycor() > 300:
            level += 1
            self.clear()
            self.level()
            player.goto(0, -270)
            Cars.increase_speed(self)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, "center", FONT)
