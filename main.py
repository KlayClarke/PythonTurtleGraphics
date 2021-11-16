from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
turtle.colormode(255)
turtle.speed('fastest')


def draw_spirograph(size_of_gap):
    n = 0
    for i in range(int(360 / size_of_gap)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        turtle.color(random_color)
        turtle.circle(100)
        turtle.setheading(n)
        n += size_of_gap


draw_spirograph(2)

screen = Screen()
screen.exitonclick()
