from tkinter import *
import pandas
import random

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Arial", 40, "italic")
FONT_2 = ("Arial", 60, "bold")
LANGUAGE = {"front": "French", "back": "English"}


# Functions
def gen_new_word():
    global random_word, word_dict, word_text
    random_word = random.choice(word_dict)
    canvas.itemconfig(word_text, text=f"{random_word['French']}")

# -------------FLIP MECHANISM-----------#



# Set Up User Interface
root = Tk()
root.config(width=850, height=576, padx=50, pady=50, background="black")
timer = root.after(3000)

# Ingest CSV data
words = pandas.read_csv("data/french_words.csv")
word_dict = words.to_dict(orient="records")
print(word_dict)

random_word = random.choice(word_dict)
print(random_word)

card_img = PhotoImage(file="images/card_front.png")

canvas = Canvas(root)
canvas.config(width=850, height=576, highlightthickness=0, background="black")
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_image(425, 280, image=card_img)

canvas.create_text(400, 150, text=f"French", font=FONT_1)
word_text = canvas.create_text(400, 263, text=f"{random_word['French']}", font=FONT_2)

cross_img = PhotoImage(file="images/right.png")
cross_button = Button(image=cross_img, highlightthickness=0, background="black", command=gen_new_word)
cross_button.grid(column=1, row=1)
check_img = PhotoImage(file="images/wrong.png")
check_button = Button(image=check_img, highlightthickness=0, background="black")
check_button.grid(column=0, row=1)



root.mainloop()
