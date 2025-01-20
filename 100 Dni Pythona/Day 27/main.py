from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500,300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text='I Am a label', font=("Arial", 24, "bold"))
my_label["text"] = 'new text'
my_label.config(text="New text")
my_label.grid(column=0, row=0)


# def button_click():
#     my_label["text"] = input.get()

# Button
button = Button(text="Click me")
button.grid(column = 1, row =1)

button2 = Button(text='New Button')
button2.grid(column=2, row=0)
# Input
input = Entry(width = 10)
input.grid(column=3,row=2)


window.mainloop()