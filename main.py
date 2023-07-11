from turtle import Turtle, Screen

angela_the_turtle = Turtle()
angela_the_turtle.shape("turtle")
angela_the_turtle.color("coral")


for i in range(4):
    angela_the_turtle.right(90)
    angela_the_turtle.forward(100)



screen = Screen()
screen.exitonclick()