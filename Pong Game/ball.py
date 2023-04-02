from turtle import *
from random import *


class Ball:
    def __init__(self) -> None:
        self.ball = Turtle(shape="circle")
        self.ball.color("white")
        self.ball.shapesize(1, 1)
        self.ball.penup()
        self.ch = 0
        self.angle = 0
        self.writer = Turtle(visible=False)
        self.writer.color("white")

    def move_ball(self):
        self.ball.forward(20)
        print(self.ball.pos())

    def set_ball(self):
        self.ch = choice((1, 2))
        if self.ch == 1:
            self.ball.goto(-20, 0)
            self.angle = randint(135, 225)
            self.ball.setheading(self.angle)
        else:
            self.ball.goto(20, 0)
            self.angle = choice((randint(0, 45), randint(315, 360)))
            self.ball.setheading(self.angle)

    def collision_with_paddle(self, p1, p2, sc1, sc2):
        paddle1_x = p1.paddle.xcor()
        paddle1_y = p1.paddle.ycor()
        paddle2_x = p2.paddle.xcor()
        paddle2_y = p2.paddle.ycor()

        if (
            self.ball.distance((paddle1_x, paddle1_y)) < 30
            or self.ball.distance((paddle2_x, paddle2_y)) < 30
        ):
            if self.ball.heading() >= 0 and self.ball.heading() <= 45:
                self.ball.setheading(self.ball.heading() + 90)
                sc2.update_score()
                return True
            elif self.ball.heading() >= 135 and self.ball.heading() <= 180:
                self.ball.setheading(self.ball.heading() - 90)
                sc1.update_score()
                return True
            elif self.ball.heading() >= 180 and self.ball.heading() <= 225:
                self.ball.setheading(self.ball.heading() + 90)
                sc1.update_score()
                return True
            elif self.ball.heading() >= 315 and self.ball.heading() <= 360:
                self.ball.setheading(self.ball.heading() - 90)
                sc2.update_score()
                return True
            else:
                return False

    def collision_with_wall(self):
        if self.ball.ycor() >= 340 or self.ball.ycor() <= -340:
            if self.ball.heading() > 45 and self.ball.heading() < 90:
                self.ball.setheading(self.ball.heading() + 270)
            elif self.ball.heading() > 90 and self.ball.heading() < 135:
                self.ball.setheading(self.ball.heading() + 90)
            elif self.ball.heading() > 225 and self.ball.heading() < 270:
                self.ball.setheading(self.ball.heading() - 270)
            elif self.ball.heading() > 270 and self.ball.heading() < 315:
                self.ball.setheading(self.ball.heading() - 90)

    def out_of_screen(self):
        if self.ball.xcor() < -360:
            self.writer.write(
                "Game Over\nPlayer 2 Wins!", False, "center", ("Arial", 16, "bold")
            )
            return False
        elif self.ball.xcor() > 360:
            self.writer.write(
                "Game Over\nPlayer 1 Wins!", False, "center", ("Arial", 16, "bold")
            )
            return False
        else:
            return True
