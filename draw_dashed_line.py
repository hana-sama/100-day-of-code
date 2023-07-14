from turtle import Turtle, Screen


t = Turtle()


def draw_dashed_lines():
    for i in range(15):
        t.pendown()
        t.forward(5)
        t.penup()
        t.forward(5)


for i in range(4):
    t.right(90)
    draw_dashed_lines()

screen = Screen()
screen.exitonclick()