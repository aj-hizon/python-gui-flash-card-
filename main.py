from tkinter import *
import pandas
import csv
import random 

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv(r"C:\Users\Hizon\Desktop\Coding\python\day-31- flash-card-project\data\french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

#------------------------------ NEXT CARD ---------------------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


#------------------------------ UI SETUP ----------------------------------#

window = Tk()
window.title("Quicky")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0,columnspan=2)
card_front = PhotoImage(file=r"C:\Users\Hizon\Desktop\Coding\python\day-31- flash-card-project\images\card_front.png")
card_back = PhotoImage(file=r"C:\Users\Hizon\Desktop\Coding\python\day-31- flash-card-project\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="word", font=('Ariel', 60, 'bold' ) )

wrong_image = PhotoImage(file=r"C:\Users\Hizon\Desktop\Coding\python\day-31- flash-card-project\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1 , column=0)



right_image = PhotoImage(file=r"C:\Users\Hizon\Desktop \Coding\python\day-31- flash-card-project\images\right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=1 )

next_card()



window.mainloop()