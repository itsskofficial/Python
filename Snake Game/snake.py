from turtle import *
from random import *
from time import *


class Snake:
    def __init__(self) -> None:
        self.snake_parts = []
        self.s = Screen()
        self.j = 10
        self.w = Turtle(visible=False)
        self.w.color("white")
        self.collision = False

    def create_snake(self):
        for i in range(3):
            t = Turtle(shape="square")
            t.penup()
            t.shapesize(0.5, 0.5)
            t.color("white")
            t.goto(self.j, 0)
            self.j -= 10
            self.snake_parts.append(t)

    def create_snake_part(self):
        t = Turtle(shape="square")
        t.penup()
        t.shapesize(0.5, 0.5)
        t.goto(self.snake_parts[-1].position())
        self.snake_parts.append(t)
        t.color("white")

    def up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)

    def left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)

    def right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)

    def down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)

    def move_snake(self):
        for i in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[i].goto(self.snake_parts[i - 1].pos())
        self.snake_parts[0].forward(10)

    def start_game(self):
        self.w.write("Welcome to Snake!", False, "center", ("Arial", 20, "bold"))
        sleep(2)
        self.w.clear()

    def check_collision_wall(self):
        if (
            self.snake_parts[0].xcor() > 240
            or self.snake_parts[0].xcor() < -240
            or self.snake_parts[0].ycor() > 240
            or self.snake_parts[0].ycor() < -240
        ):
            self.w.write("Game Over!", False, "center", ("Arial", 20, "bold"))
            sleep(2)
            return False
        else:
            return True

    def check_collision_tail(self):
        for i in range(1, len(self.snake_parts)):
            if self.snake_parts[0].distance(self.snake_parts[i]) == 0:
                self.w.write("Game Over!", False, "center", ("Arial", 20, "bold"))
                sleep(2)
                self.collision = True
                break
        if self.collision == True:
            return False
        else:
            return True

    def food_eaten(self, food, score):
        if self.snake_parts[0].distance(food.food) < 15:
            food.refresh()
            self.create_snake_part()
            score.update_score()
