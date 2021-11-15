from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
turtle.colormode(255)
tim.speed('fastest')
tim.pensize(15)


directions = [0, 90, 180, 270]


def turtle_walk():
    for i in range(2500):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        tim.color(random_color)
        tim.forward(10)
        tim.setheading(random.choice(directions))


turtle_walk()

screen = Screen()
screen.exitonclick()
