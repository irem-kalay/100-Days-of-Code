from turtle import Turtle, Screen

tim= Turtle()


for index in range(25):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



screen = Screen()
screen.exitonclick()
