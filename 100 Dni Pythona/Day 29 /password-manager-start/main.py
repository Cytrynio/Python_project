from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    all_characters = letters + numbers + symbols

    password_list = [random.choice(all_characters) for _ in range(nr_numbers + nr_letters + nr_symbols)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data= {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)

# --------------------------SEARCH BUTTON ----------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username/Email:{email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



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
website_input = Entry(width=24)
website_input.grid(column=1,row=1)
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1,row=2, columnspan=2)
email_username_input.insert(0, 'xxx@wp.pl')

password_input = Entry(width=24)
password_input.grid(column=1,row=3)


# Buttons
search_btn = Button(text="Search",width=7,command=find_password)
search_btn.grid(column=2,row=1)

generate_password_btn = Button(text="Generate",width=7,command=password_generator)
generate_password_btn.grid(column=2,row=3)

add_btn= Button(text="Add",width=32,command=save)
add_btn.grid(columnspan=2, column=1,row=4)



window.mainloop()