from turtle import *
from snake import *
from random import *


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...
    ) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.f = open(
            "high_score.txt",
        )
        self.setpos(0, 225)
        self.high_score = self.f.read()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            "center",
            ("Times New Roman", "16", "bold"),
        )

    def update_high_score(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            self.f.close()
            f = open("high_score.txt", "w")
            f.write(self.high_score)
            f.close()
