import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim= Turtle()
tim.speed(1000)

def random_colors():
    r= random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor= (r,g,b)
    return randomcolor

def draw_spirograph(gap):    #360 degrees will be devided by number of gap
    for index in range(int(360/gap)):
        tim.color(random_colors())
        tim.circle(50)
        tim.left(gap)


draw_spirograph(5) #the least integer gap you select, the most circles you get

screen = Screen()
screen.exitonclick()
