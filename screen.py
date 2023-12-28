from turtle import Turtle, Screen


# screen=Screen()
class Screen1():
    def __init__(self):
        pass

    def sccrr(self):
        print("Hello")
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(1000, 700)
        line = Turtle()
        line.penup()
        line.shape("square")
        line.color("white")
        line.teleport(0, 400)
        y1 = 350
        for i in range(18):
            line.speed("fastest")
            line.pendown()
            y1 -= 20
            line.goto(0, y1)
            line.penup()
            y1 -= 20
            line.goto(0, y1)
            line.pendown()
            line.width(5)
        # screen.exitonclick()