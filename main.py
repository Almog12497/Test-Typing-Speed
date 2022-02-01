import tkinter as tk
from get_words import Text
import time

# Get random words
paragraph = Text()
paragraph = paragraph.form_text()

# Init variables
game_start = False
correct_words = []
counter = 0

def start():
    global game_start
    global timer

    #Starts a timer from the sec the game stars
    timer = time.time()
    box['text'] = paragraph[:6]
    box.grid(row=2,column=0, pady=20)
    # Disable button after clicking
    start_btn["state"] = tk.DISABLED
    game_start = True
    # Ends the game after 60 secs
    window.after(60000, end)


def update(event):
    global counter
    global game_start

    if game_start:
        # Get current time, check the word and see if its the same as the first word in the box.
        now = time.time()
        temp = entry.get().strip()
        if paragraph[counter] == temp:
            correct_words.extend(temp)
        # Clears the entry box
        entry.delete(0, 'end')
        counter += 1
        box['text'] = paragraph[counter:counter+6]
        # Calculates WPM
        wpm['text'] = str(int((len(correct_words) / (now - timer))*(60-(now - timer))))


def end():
    global game_start

    # Displayed final_wpm
    final_wpm = wpm.cget("text")
    box['text'] = f"FINAL SCORE: {final_wpm}"
    game_start = False
    start["state"] = tk.ENABLE

#Init window
window = tk.Tk()
window.minsize(800, 600)
window.title("Type Racer")
window.configure(bg="#C0D8C0")
window.bind("<space>", update)


# All the widgets that are on the screen
title = tk.Label(text="Welcome to Typing Test, click on the button to start!", font=("Arial", 25), bg="#C0D8C0")
title.grid(row=0, column=0, sticky="N", padx=20, pady=20, columnspan=3)

start_btn = tk.Button(text="Start", font=("Arial", 25), fg="#DD4A48", bg="#F5EEDC",command=start)
start_btn.grid(row=1, column=0, sticky="N", padx=20, pady=20)

box = tk.Label(width=30, height=8,wraplength=150, borderwidth=2, relief="solid", font=("Arial", 18), bg="#F5EEDC")
box.grid(row=2,column=0, pady=20, columnspan=3)

entry = tk.Entry(font=("Arial", 25))
entry.grid(row=3, column=0, columnspan=3)

wpm_label = tk.Label(text="WPM:", font=("Arial", 18))
wpm_label.grid(row=1,column=1)
wpm = tk.Label(text=0,borderwidth=2, relief="solid", font=("Arial", 18))
wpm.grid(row=1,column=2)

window.mainloop()