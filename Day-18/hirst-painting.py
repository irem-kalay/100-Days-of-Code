import random
import colorgram
import turtle as t
from turtle import Screen

my_turtle= t.Turtle()
my_turtle.speed("fastest")
t.colormode(255)
my_turtle.hideturtle()

#the color list that taken from hirst painting
color_list= [ (166, 151, 135), (222, 206, 123), (143, 101, 88), (120, 88, 99), (83, 89, 127), (196, 96, 83)]


def get_random_color():
    random_number = random.randint(0, 5)
    r= int(color_list[random_number][0])
    g= int(color_list[random_number][1])
    b= int(color_list[random_number][2])

    new_color= (r,g,b)
    return new_color


my_turtle.teleport(-225, -200) #for the inital start place, I used teleport method

def draw_line():
    for row in range(0,10):
        for i in range (0, 10):
            color= get_random_color()
            my_turtle.pen(pencolor=color)

            my_turtle.begin_fill()
            my_turtle.circle(10)
            my_turtle.fillcolor(color)
            my_turtle.end_fill()

            my_turtle.penup()
            my_turtle.forward(50)
            my_turtle.pendown()

        my_turtle.left(90)
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.teleport(-225)
        my_turtle.right(90)
        my_turtle.pendown()

draw_line()




# Extract 6 colors from an image.
#colors = colorgram.extract('hirst_painting.jpg', 10)


#rgb_colors=[]
#for color in colors:
#    r= color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color=(r,g,b)
#    rgb_colors.append(new_color)

#print(rgb_colors)



screen= Screen()
screen.exitonclick()
