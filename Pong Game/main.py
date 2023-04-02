from turtle import *
from ball import *
from paddle import *
from time import *
from scoreboard import *

s = Screen()
s.setup(700, 700)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)
play_game = "Yes"
game_is_on = True

while play_game == "Yes":
    p1 = Paddle()
    p2 = Paddle()
    b = Ball()
    sc1 = Scoreboard((-175, 300))
    sc2 = Scoreboard((175, 300))
    p1.set_paddle(-300, 0, 90)
    p2.set_paddle(300, 0, 270)
    b.set_ball()
    s.listen()
    s.onkey(p1.move_paddle_down1, "s")
    s.onkey(p2.move_paddle_up1, "Up")
    s.onkey(p1.move_paddle_up1, "w")
    s.onkey(p2.move_paddle_down1, "Down")
    s.onkeypress(p1.move_paddle_up2, "w")
    s.onkeypress(p1.move_paddle_down2, "s")
    s.onkeypress(p2.move_paddle_up2, "Up")
    s.onkeypress(p2.move_paddle_down2, "Down")
    while game_is_on:
        s.update()
        sleep(0.1)
        b.move_ball()
        c1 = b.collision_with_paddle(p1, p2, sc1, sc2)
        c2 = b.collision_with_wall()
        game_is_on = b.out_of_screen()
    play_game = s.textinput("Game Over!", "Do you want to play again? ")
s.bye()
