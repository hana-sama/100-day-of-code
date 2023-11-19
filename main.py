import tkinter

# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

def new_button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
new_button = tkinter.Button(text="New Button", command=new_button_clicked)
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=4, row=2)

window.mainloop()

