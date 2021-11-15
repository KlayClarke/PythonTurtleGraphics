from turtle import Turtle, Screen

tim = Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.right(angle)
        tim.forward(100)

draw_shape(4)
draw_shape(5)
draw_shape(6)
draw_shape(7)
draw_shape(8)

screen = Screen()
screen.exitonclick()
