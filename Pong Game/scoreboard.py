from turtle import *


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(pos)
        self.high_score = 0

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", ("Times New Roman", "25", "bold"))
