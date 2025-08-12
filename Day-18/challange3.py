from turtle import Turtle, Screen

tim= Turtle()


edge= 3
colors= ["red", "purple", "blue", "green", "yellow", "orange", "pink", "brown"]

for index in range(8):
    tim.color(colors[edge - 3])
    for shape in range(edge):
        degree= 360/edge
        tim.right(degree)
        tim.forward(100)
    edge= edge+1


screen = Screen()
screen.exitonclick()
