import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
# tim.shape("turtle")
# tim.color("red")

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.right(45)
#     tim.forward(10)
#     tim.pendown()
#
#
# colors= ["royal blue","red","magenta", "gold","green yellow","dark green","dark slate blue","rosy brown","coral","green"]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

#
# direction = [0,90,180,270]
#
# for _ in range(300):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
#     tim.pensize(10)
#     tim.speed("fastest")


def draw_sphirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

print(draw_sphirograph(5))

# for num_sides in range(3,11):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#         tim.color(colors[num_sides])
#

screen = Screen()
screen.exitonclick()


