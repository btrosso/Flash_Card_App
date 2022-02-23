from tkinter import *
import pandas
import random

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Arial", 40, "italic")
FONT_2 = ("Arial", 60, "bold")


# Ingest CSV data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}


# Functions
def next_card():
    global current_card, flip_timer, to_learn
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_img_front)
    flip_timer = root.after(3000, func=flip_card)


def remove():
    global current_card, to_learn
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_img_back)


# Set Up User Interface
root = Tk()
root.config(width=850, height=576, padx=50, pady=50, background="black")
timer = root.after(3000)

flip_timer = root.after(3000, func=flip_card)

card_img_front = PhotoImage(file="images/card_front.png")
card_img_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(root)
canvas.config(width=850, height=526, highlightthickness=0, background="black")
canvas.grid(column=0, row=0, columnspan=2)
card_image = canvas.create_image(400, 263, image=card_img_front)

card_title = canvas.create_text(400, 150, text="", font=FONT_1)
card_word = canvas.create_text(400, 263, text="", font=FONT_2)

right_img = PhotoImage(file="images/right.png")
check_button = Button(image=right_img, highlightthickness=0, background="black",
                      command=lambda: [next_card(), remove()])
check_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_img, highlightthickness=0, background="black", command=next_card)
cross_button.grid(column=0, row=1)


next_card()

root.mainloop()
