from tkinter import *
from requests import get

# =======================================================================================
# Choosing suffix
# =======================================================================================
suffix = None


def entered_suffix(button):
    global suffix
    suffix = entry.get().strip().lower().strip("'")
    if len(suffix) < 2:
        error_label.config(text="Please enter at least 2 characters")
        error_label.pack(pady=20, padx=20)
        entry.delete(0, END)
        return
    for letter in suffix:
        if ord(letter) < 97 or ord(letter) > 122:
            error_label.config(text="Please enter valid characters (A-Z)")
            error_label.pack(pady=20, padx=20)
            entry.delete(0, END)
            return
    window.destroy()


window = Tk()
window.config(bg="black", padx=50, pady=50)
entry = Entry()
label = Label(text="Enter your suffix", bg="black", fg="white", font=("Arial", 30, "normal"))
error_label = Label(text="Please enter at least 2 characters",
                    bg="black",
                    fg="white",
                    font=("Arial", 15, "normal"))
label.pack(padx=30, pady=30)
entry.pack(padx=30, pady=30)
window.bind("<Return>", entered_suffix)
window.bind("'", entered_suffix)

entry.focus()

window.mainloop()

# =======================================================================================
# Game Process
# =======================================================================================
score = 0
already_said_words = []
unknown_words = []


def entered(button):
    global score
    word = entry.get().lower().strip("'").strip()
    entry.delete(0, END)
    if word not in already_said_words:
        response = get(url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    else:
        return
    if response.status_code == 200 and word[:len(suffix)] == suffix:
        score += 1
        label_score.config(text=f"{score}")
        already_said_words.append(word)
        if button.char == "'":
            unknown_words.append(word)


def end_game():
    with open("to_learn.txt", "w") as file:
        if len(unknown_words) != 0:
            file.write("Unknown words:\n\n")
            for word in unknown_words:
                file.write(f"{word}\n")
        else:
            file.write("No unknown words")
    try:
        with open(f"./words/{suffix}_words.txt", "r+") as file:
            word_list = file.read().split("\n")
            words_to_write = [word for word in already_said_words if word not in word_list]
            for word in words_to_write:
                file.write(f"{word}\n")
    except FileNotFoundError:
        with open(f"./words/{suffix}_words.txt", "w") as file:
            for word in already_said_words:
                file.write(f"{word}\n")
    window.destroy()


window = Tk()
window.config(bg="black", padx=100, pady=30)
label_suffix = Label(text=suffix, font=("Arial", 50, "normal"), bg="black", fg="white")
label_score = Label(text=f"{score}", font=("Arial", 50, "normal"), bg="black", fg="white")
entry = Entry()
button = Button(text="END", padx=10, pady=10, bg="black", fg="red", command=end_game)

label_score.pack(padx=40, pady=40)
entry.pack(padx=40, pady=40)
label_suffix.pack(padx=40, pady=40)
button.pack()

entry.focus()

window.bind("<Return>", entered)
window.bind("'", entered)

window.mainloop()

