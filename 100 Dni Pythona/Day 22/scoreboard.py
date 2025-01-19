from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"Level: {self.player_score}", align="left", font=FONT)

    def point_add(self):
        self.player_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",font =FONT)