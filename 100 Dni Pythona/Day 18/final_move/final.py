# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
from turtle import Turtle, Screen
import turtle

colors_list =[ (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

brush = Turtle()
turtle.colormode(255)
brush.speed("fastest")
brush.penup()
brush.hideturtle()


brush.setheading(225)
brush.forward(300)
brush.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    brush.dot(20, random.choice(colors_list))
    brush.fd(50)
    if dot_count % 10 == 0:
        brush.setheading(90)
        brush.fd(50)
        brush.setheading(180)
        brush.fd(500)
        brush.setheading(0)

screen = Screen()
screen.exitonclick()
