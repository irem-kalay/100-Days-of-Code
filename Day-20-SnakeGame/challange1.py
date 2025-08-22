from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#create a snake body
snake = Turtle(shape="arrow")
snake.hideturtle()
snake.speed("fastest")
snake.penup()

def draw_square():
    snake.fillcolor("white")
    snake.pencolor("white")

    snake.begin_fill()
    snake.setheading(0)
    for _ in range(0,4):
        snake.right(90)
        snake.forward(20)

    snake.setheading(180)
    snake.forward(20)
    snake.end_fill()

#3 squares for initial snake
for i in range(0,3):
    draw_square()




screen.exitonclick()