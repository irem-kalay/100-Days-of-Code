import turtle as t
import random
from turtle import Screen

tim= t.Turtle()
t.colormode(255)

def random_colors():
    r= random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= (r,g,b)

    return random_color

directions=["north", "east", "south", "west"]
#colors=["brown", "pink", "purple", "green", "yellow", "orange"]
forward_direction= 0
current_direction= random.choice(directions)

def direction(random_direction):
    if random_direction== directions[0]:
        tim.setheading(0)
    elif random_direction== directions[1]:
        tim.setheading(90)
    elif random_direction== directions[2]:
        tim.setheading(180)
    elif random_direction== directions[3]:
        tim.setheading(270)


tim.pensize(5)
tim.speed(10)

for index in range(200):
    new_direction=random.choice(directions)
    direction(new_direction) #having random direction

    if new_direction!= current_direction:
        tim.color(random_colors())

    current_direction= new_direction
    tim.forward(25)



screen = Screen()
screen.exitonclick()