from turtle import Turtle, Screen

tim= Turtle()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_counter_clockwise():
    tim.left(10)#I can fix the degree if I want to

def turn_clockwise():
    tim.right(10)


def clear_all():
    tim.clear()
    tim.teleport(0,0)
    tim.setheading(0)

screen= Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun= move_backward)
screen.onkey(key="a", fun= turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun= clear_all)





screen.exitonclick()