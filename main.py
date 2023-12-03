from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers

        shuffle(password_list)

        password = "".join(password_list)

        password_input.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \n Is it okay to save?")
        if is_ok == True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
                username_input.insert(0, "angela@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

# ----------- Create labels, entries, and buttons ---------- #

# Labels
website = Label(text="Website:", font=("Colibri", 10, "bold"), bg=YELLOW)
website.grid(column=0, row=1, sticky="w")
username = Label(text="Email/Username:", font=("Colibri", 10, "bold"), bg=YELLOW)
username.grid(column=0, row=2, sticky="w")
password = Label(text="Password:", font=("Colibri", 10, "bold"), bg=YELLOW)
password.grid(column=0, row=3, sticky="w")

# Entries
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="ew")
username_input = Entry(width=35)
username_input.insert(0, "angela@email.com")
username_input.grid(column=1, row=2, columnspan=2, sticky="ew")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1, sticky="ew")

# Buttons
password_generate = Button(text="Generate Password", bg="white", command=generate_password)
password_generate.grid(column=2, row=3, columnspan=1, sticky="ew")
add = Button(text="Add", bg="white", width=50, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()