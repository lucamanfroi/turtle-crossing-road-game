from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time

car_speed = 2

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.colormode(255)

player = Player()
scoreboard = Scoreboard()
car = Car()
car.hideturtle()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

game_on = True
while game_on:
    time.sleep(0.01)
    car.new_car()
    for i in car.all_cars:
        if i.distance(player) <= 26:
            scoreboard.game_over()
            game_on = False
        if i.xcor() < -300:
            i.hideturtle()
            car.all_cars.remove(i)
        i.move(car_speed)
        screen.update()
    if player.ycor() >= 270:
        for i in car.all_cars:
            i.hideturtle()
        car.all_cars = []
        car_speed += 1
        car.max_range *= 0.9
        scoreboard.refresh()
        player.goto(0, -280)

screen.exitonclick()
