import random
from tkinter import *
import  pandas
BACKGROUND_COLOR = "#B1DDC6"

# READING DATA
current_card = {}
words_to_learn = {}

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = df.to_dict(orient="records")

# Button function

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(language_name_text, text='French',fill='black')
    canvas.itemconfig(word_text, text=current_card["French"], fill='black')
    canvas.itemconfig(card_bg,image= front_card_png)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(language_name_text, text='English',fill='white')
    canvas.itemconfig(word_text, text=current_card["English"],fill='white')
    canvas.itemconfig(card_bg, image=back_card_png)

def right_guess():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv('data/words_to_learn', index=False)
    next_card()

# TKINTER CONFIG
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

# FLASHCARD CANVAS
canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
back_card_png = PhotoImage(file="images/card_back.png")
front_card_png = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400,263, image=front_card_png)
language_name_text = canvas.create_text(400,150,text='', font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)



# BUTTONS
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=right_guess)
right_button.grid(column=1,row=1)

wrong_button_image = PhotoImage(file="images/wrong.png",)
wrong_button = Button(image=wrong_button_image,command=next_card)
wrong_button.grid(column=0,row=1)

next_card()

window.mainloop()