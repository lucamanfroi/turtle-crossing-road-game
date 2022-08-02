from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-235, 265)
        self.hideturtle()
        self.current_level = 1
        self.scoreboard()

    def scoreboard(self):
        self.write(arg=f'LEVEL: {self.current_level}', align='center', font=('Verdana', 15, 'bold'))

    def refresh(self):
        self.clear()
        self.current_level += 1
        self.write(arg=f'LEVEL: {self.current_level}', align='center', font=('Verdana', 15, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=('Verdana', 20, 'bold'))
