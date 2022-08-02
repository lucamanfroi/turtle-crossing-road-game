from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.max_range = 20

    def new_car(self):
        random_chance = random.randint(1, int(self.max_range))
        if random_chance == 1:
            new_car = Car()
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_car.goto(310, random.randint(-230, 250))
            self.all_cars.append(new_car)

    def move(self, speed):
        self.backward(speed)
