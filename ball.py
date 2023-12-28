from turtle import Turtle, Screen
# from paddle import Paddle, PADDLE_SEGMENT, KEY_PADDLE
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 700)


class Box():
    def __init__(self) -> None:
        self.x_move=10
        self.y_move=10
        self.move_speed=0.01


    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape("square")
        self.ball.penup()
        self.ball.color("white")
        # self.ball.speed("slowest")

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def after_hit_y(self):
        self.y_move *= -1
        self.move_speed*=0.9

    def after_hit_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.ball.goto(0,0)
        self.move_speed=0.01
# pad=Paddle()
# pad.second_user_paddle()

# b1=Box()
# b1.create_ball()
# b1.move()
# screen.delay(1)
# game_on=True
# while game_on:
#     for i in range(len(KEY_PADDLE)):
#         if b1.ball.distance(KEY_PADDLE[i])<15:
#             print("gello")
#             b1.after_hit()
# game_on=False
# screen.exitonclick()