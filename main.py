from tkinter import *
import pandas as pd
from random import randint, choice
import os
BACKGROUND_COLOR = "#B1DDC6"

# Global variables
current_card = {}
score = 0
learnt_words_list = []
to_learn = {}

# ---------- Generating words list ---------- #
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/french_words.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

def checked_card():
    global current_card, score, learnt_words_list
    learnt_words_list.append(current_card)
    data = pd.DataFrame(learnt_words_list)
    data.to_csv("data/words_learnt.csv", index=False)
    # print(learnt_words_list)
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------- generating a new card ---------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

# ---------- Flip card---------- #
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Card
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# Buttons
unknown_button = Button(bg=BACKGROUND_COLOR, image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(bg=BACKGROUND_COLOR,image=right_image, highlightthickness=0, command=checked_card)
known_button.grid(row=1, column=1)

next_card()
# window.after(3000, flip_card)
window.mainloop()

