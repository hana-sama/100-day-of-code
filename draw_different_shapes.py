from turtle import Turtle, Screen
import random

t = Turtle()

colors = ["cornflower blue", "green yellow", "orange", "salmon", "hot pink", "dark orchid", "dark slate blue", "firebrick", "lawn green", "yellow", "cadet blue", "seashell", "dark blue"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for i in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(i)

screen = Screen()
screen.exitonclick()