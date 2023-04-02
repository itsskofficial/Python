from turtle import *
from time import *
from player import *
from cars import *

s = Screen()
s.setup(600, 600)
play_again = "Yes"

while play_again == "Yes":
    s.clear()
    s.tracer(0)
    p = Player()
    scoreboard = Scoreboard()
    game_on = True
    s.onkey(p.move_turtle, "Up")
    s.listen()
    while game_on:
        sleep(0.1)
        s.update()
        scoreboard.level()
        car = Cars()
        car.move_cars()
        scoreboard.level_increase(p)
        game_on = p.detect_collision()
    play_again = s.textinput("Game Over!", "Do you want to play again?")

s.bye()
