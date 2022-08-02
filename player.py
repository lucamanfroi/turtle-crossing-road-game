from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        new_y = self.ycor() + 15
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 15
        self.sety(new_y)
