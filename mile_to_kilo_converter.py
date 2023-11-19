import tkinter

def button_clicked():
    kilometer = f"{int(input.get()) * 1.609344:.2f}"
    output.config(text=kilometer)
    


# Creating window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=250, pady=50)

# Input
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

# Label
label_for_input = tkinter.Label(text="Miles")
label_for_input.grid(column=2, row=0)

prelabel_for_output = tkinter.Label(text="is equal to")
prelabel_for_output.grid(column=0, row=1)

output = tkinter.Label(text="0", font=("Arial", 24, "bold"))
output.grid(column=1, row=1)

after_label_for_output = tkinter.Label(text="Km")
after_label_for_output.grid(column=3, row=1)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
window.mainloop()
