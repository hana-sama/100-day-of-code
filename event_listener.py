from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mutiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(5, 34, add)

print(result)