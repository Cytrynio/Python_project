from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_png)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0,row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0,row=2)

password_label = Label(text='Password:')
password_label.grid(column=0,row=3)

# Inputs
website_input = Entry(width=35)
website_input.grid(column=1,row=1, columnspan=2)
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1,row=2, columnspan=2)
email_username_input.insert(END)

password_input = Entry(width=24)
password_input.grid(column=1,row=3)


# Buttons

generate_password_btn = Button(text="Generate",width=8)
generate_password_btn.grid(column=2,row=3)

add_btn= Button(text="Add",width=32)
add_btn.grid(columnspan=2, column=1,row=4)







window.mainloop()