import random
from ball import Box
from turtle import Screen, Turtle, mainloop
from screen import Screen1
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)

scoreboard1=ScoreBoard()
sc1 = Screen1()
sc1.sccrr()
l_paddle = Turtle()
l_paddle.color("white")
l_paddle.shape("square")
l_paddle.penup()
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.teleport(-480, 50)

r_paddle = Turtle()
r_paddle.color("white")
r_paddle.shape("square")
r_paddle.penup()
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.teleport(480, 50)


def move_paddle_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)


def move_paddle_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)


def move_paddle_up1():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)


def move_paddle_down1():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)


screen.listen()
screen.onkey(fun=move_paddle_up, key="w")
screen.onkey(fun=move_paddle_down, key="s")

screen.onkey(fun=move_paddle_up1, key="Up")
screen.onkey(fun=move_paddle_down1, key="Down")

screen.tracer(1)
b1=Box()
b1.create_ball()
# # b1.ball.speed("slow")
# # b1.move()
# # # screen.tracer(0)

game_on = True
while game_on:
    screen.update()
    time.sleep(b1.move_speed)
    b1.move()

    if b1.ball.ycor()>320 or b1.ball.ycor()<-320:
        b1.after_hit_y()

    if b1.ball.distance(r_paddle) < 50 and b1.ball.xcor()>470 or b1.ball.distance(l_paddle)<50 and b1.ball.xcor()<-470:
        b1.after_hit_x()

    if b1.ball.xcor()>500:
        b1.reset_position()
        b1.after_hit_x()
        scoreboard1.l_point()
    if b1.ball.xcor()<-500:
        b1.reset_position()
        b1.after_hit_x()
        scoreboard1.r_point()




mainloop()
screen.exitonclick()
