import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
# print(states_data)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
states = states_data.state
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    asnwer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name? ").title()
    if asnwer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if asnwer_state in all_states:
        guessed_states.append(asnwer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = states_data[states_data.state == asnwer_state]
        t.goto(int(data.x), int(data.y))
        t.write(data.state.item())

screen.exitonclick()