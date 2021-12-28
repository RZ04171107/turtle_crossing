from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_NUM = 20


class Car(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(xcor, ycor)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())


class CarManager:
    def __init__(self):
        self.cars = []
        self.place_cars()

    def place_cars(self):
        for _ in range(CARS_NUM):
            x_rdm = random.randint(-300, 300)
            y_rdm = random.randint(-250, 250)
            car = Car(x_rdm, y_rdm)
            self.cars.append(car)

    def place_cars_edge(self):
        y_rdm = random.randint(-250, 280)
        car = Car(300, y_rdm)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()
