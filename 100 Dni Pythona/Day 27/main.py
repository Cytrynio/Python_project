import  tkinter

from PIL.ImageOps import expand

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(500,300)



my_label = tkinter.Label(text='I Am a label', font=("Arial", 24, "bold"))
my_label.pack(expand=True)










window.mainloop()