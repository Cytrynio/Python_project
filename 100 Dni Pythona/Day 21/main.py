from time import sleep
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import  time


# SCREEN SETTINGS
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)



paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")

screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_add()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_add()














screen.exitonclick()