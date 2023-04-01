import random
import colors
import turtle

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)


def draw():
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(colors.rgb_colors))
        timmy.penup()
        timmy.forward(30)


def move_to_start():
    timmy.setheading(90)
    timmy.forward(30)
    timmy.setheading(180)
    timmy.forward(300)


for _ in range(10):
    timmy.hideturtle()
    draw()
    move_to_start()
    timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()

