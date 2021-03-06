from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.pendown()
        self.level_num = 1
        self.write(f"Level: {self.level_num}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.level_num += 1
        self.write(f"Level: {self.level_num}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", align="center", font=FONT)
