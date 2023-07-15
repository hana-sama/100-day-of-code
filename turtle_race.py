from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "lime", "dark slate blue"]
y_positions = [-100, -70, -40, -10, 20, 50, 80, 110]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

print(all_turtles)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is {winning_color} turtle")
            else:
                print(f"You've lost! The winner is {winning_color} turtle")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()