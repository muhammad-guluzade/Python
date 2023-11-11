
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

counter = 1
time_left = 1500
corn = True
check_marks = ""


def make_corn_true():
    global corn, title_label
    corn = True
    title_label.config(text="Work", fg=GREEN)


def reset():

    global counter, time_left, corn, check_marks
    check_marks = ""
    counter = 1
    time_left = 1500
    canvas.itemconfig(timer, text="25:00")
    checkmarks_label.config(checkmarks_label, text=f"{check_marks}")
    title_label.config(text="Timer", fg=GREEN)
    corn = False


def count_down():

    global time_left, counter, corn, check_marks

    if time_left//60 < 10:
        minutes_left = f"0{time_left//60}"
    else:
        minutes_left = f"{time_left // 60}"

    if time_left-(time_left//60) * 60 < 10:
        seconds_left = f"0{time_left-(time_left//60) * 60}"
    else:
        seconds_left = f"{time_left-(time_left//60) * 60}"

    if time_left > 0 and corn:
        canvas.itemconfig(timer, text=f"{minutes_left}:{seconds_left}")
        time_left -= 1
        canvas.after(1000, count_down)
    elif corn:
        if counter % 5 == 0 and counter != 0:
            time_left = 1200
            counter = 0
            check_marks += "✓"
            checkmarks_label.config(checkmarks_label, text=f"{check_marks}")
            title_label.config(text="Break", fg=RED)
        elif counter % 2 == 0:
            time_left = 1500
            counter += 1
            title_label.config(text="Work", fg=GREEN)
        else:
            check_marks += "✓"
            checkmarks_label.config(checkmarks_label, text=f"{check_marks}")
            time_left = 300
            counter += 1
            title_label.config(text="Break", fg=RED)
        canvas.after(1000, count_down)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.config(padx=50, pady=35, bg=YELLOW)

# tomato image has width of 200 and height of 223 pixels

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# next, provide the image
# PhotoImage class is used for that

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

# create texts for our tomato (timer, title, and checkmarks)
# placing them to the correct position

timer = canvas.create_text(102, 130, text="00:00", font=("Courier", 35, "bold"), fill="white")

title_label = Label(text="Timer", font=("Courier", 50, "bold"), fg=GREEN, bg=YELLOW)
checkmarks_label = Label(text="", bg=YELLOW, fg=GREEN, font=("Courier", 18, "normal"))

title_label.grid(row=0, column=1)
checkmarks_label.grid(row=3, column=1)

# creating and placing the necessary buttons

start_button = Button(text="Start", font=("Arial", 11, "italic"))
reset_button = Button(text="Reset", font=("Arial", 11, "italic"))

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

# placing the canvas

canvas.grid(row=1, column=1)

# adding the count down mechanism
# lambda used in order to call 2 functions at the same time

start_button.config(command=lambda: [make_corn_true(), count_down()])
reset_button.config(command=reset)

window.mainloop()