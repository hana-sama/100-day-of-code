from turtle import Turtle, Screen

t = Turtle()

for i in range(30):
    t.pendown()
    t.forward(5)
    t.penup()
    t.forward(5)

screen = Screen()
screen.exitonclick()