from turtle import Turtle


ALIGN = "center"
FONT = "Courier",80,"bold"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p_1_score = 0
        self.p_2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p_2_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.p_1_score, align=ALIGN, font=FONT)

    def left_add(self):
        self.p_2_score += 1
        self.update_score()

    def right_add(self):
        self.p_1_score += 1
        self.update_score()