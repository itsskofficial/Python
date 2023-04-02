from turtle import *
from random import *
from time import *
from food import Food
from scoreboard import Scoreboard
from snake import *

play_game = "Yes"
while play_game == "Yes":
    s = Screen()
    s.setup(500, 500)
    s.bgcolor("black")
    s.title("Snake Game")
    s.tracer(0)

    snake = Snake()
    snake.create_snake()
    food = Food()
    score = Scoreboard()
    snake.start_game()
    game_is_on = True

    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.left, "Left")
    s.onkey(snake.right, "Right")
    s.onkey(snake.down, "Down")
    while game_is_on:
        s.update()
        sleep(0.1)
        snake.move_snake()
        snake.food_eaten(food, score)
        wall_collision = snake.check_collision_wall()
        tail_collision = snake.check_collision_tail()
        if wall_collision == False or tail_collision == False:
            game_is_on = False
    score.update_high_score()
    play_game = textinput("Game Over", "Do you want to play again?")
    s.clear()
s.bye()
