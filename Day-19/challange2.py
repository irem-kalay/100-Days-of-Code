import random
from turtle import Turtle, Screen

screen = Screen()
screen.listen()
#screen.onclick(key="w", fun)
screen.setup(width=500, height=400)

colors= ["red", "orange", "yellow","green", "blue", "purple"]

user_bet= screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
turtles=[]
isRaceOn= True

the_pen = Turtle()
the_pen.teleport(200, -90)
the_pen.left(90)
the_pen.forward(250) #I added a finish line to see better who have won

y_coor= -60
for index in range(0,6):
    new_player= Turtle(shape="turtle")
    new_player.penup()
    new_player.color(colors[index])
    new_player.goto(x=-200, y=y_coor)
    y_coor+=30
    turtles.append(new_player)

while isRaceOn:
    for player in turtles:
        random_distance= random.randint(0,10)
        player.forward(random_distance)

        if player.xcor()> 200:
            winning_color= player.pencolor()
            isRaceOn= False

            if winning_color == user_bet:
                print(f"You won, {winning_color} is the winning color.")
            else:
                print(f"You lost, {winning_color} is the winning color.")





screen.exitonclick()