import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
count = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    count += 1
    if count % 6 == 0:
        car_manager.place_cars_edge()

    # Detect when the turtle player collides with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the player reach the top
    if player.distance(0, 300) < 10:
        scoreboard.update_score()
        player.place_start_pos()


screen.exitonclick()