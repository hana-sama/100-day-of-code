from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:", bg="white")
website.grid(column=0, row=1, sticky="w")
username = Label(text="Email/Username:", bg="white")
username.grid(column=0, row=2, sticky="w")
password = Label(text="Password:", bg="white")
password.grid(column=0, row=3, sticky="w")

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="ew")
username_input = Entry(width=35)
username_input.insert(0, "angela@email.com")
username_input.grid(column=1, row=2, columnspan=2, sticky="ew")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1, sticky="ew")

# Buttons
password_generate = Button(text="Generate Password", bg="white")
password_generate.grid(column=2, row=3, columnspan=1, sticky="ew")
add = Button(text="Add", bg="white", width=50)
add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()