from turtle import *


class Paddle:
    def __init__(self) -> None:
        self.paddle = Turtle(shape="square")
        self.paddle.shapesize(1, 5)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.speed(0)

    def set_paddle(self, xcor, ycor, heading):
        self.paddle.goto(xcor, ycor)
        self.paddle.setheading(heading)

    def move_paddle_up1(self):
        if self.paddle.ycor() < 330 and self.paddle.ycor() < 330:
            self.paddle.setheading(90)
            self.paddle.forward(30)

    def move_paddle_down1(self):
        if self.paddle.ycor() < 330 and self.paddle.ycor() < 330:
            self.paddle.setheading(270)
            self.paddle.forward(30)

    def move_paddle_up2(self):
        if self.paddle.ycor() < 330 and self.paddle.ycor() < 330:
            self.paddle.setheading(90)
            self.paddle.forward(30)

    def move_paddle_down2(self):
        if self.paddle.ycor() < 330 and self.paddle.ycor() < 330:
            self.paddle.setheading(270)
            self.paddle.forward(30)
