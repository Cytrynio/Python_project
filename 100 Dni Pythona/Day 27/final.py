from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,200)
window.config(padx=20, pady=20)

empty_label = Label()
empty_label.grid(column=0,row=0)

input = Entry(width=10)
input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3,row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=3)

calculation = Label(text=0)
calculation.grid(column=2, row=3)

km_label = Label(text="Km")
km_label.grid(column=3,row=3)

def miles_to_km():
    result = int(input.get()) * 1.60934
    calculation["text"] = round(result,2)
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2,row=4)

window.mainloop()