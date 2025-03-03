from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fowards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_counter_clockwise():
    tim.left(20)
def turn_clockwise():
    tim.right(20)
def clear():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_fowards)
screen.onkey(key="a", fun= turn_counter_clockwise)
screen.onkey(key="d", fun= turn_clockwise)
screen.onkey(key= "s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()