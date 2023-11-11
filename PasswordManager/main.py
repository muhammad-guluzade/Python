from tkinter import *
from random import randint, shuffle
from tkinter import messagebox

import pyperclip

window = Tk()
window.config(padx=30, pady=30)

# ==================================================================
# a function for "add" button that will take the contents of entries
#  and save them into a text file
# ==================================================================


def add_user():
    global username_entry, password_entry, website_entry

    if len(username_entry.get().strip()) == 0 or len(password_entry.get().strip()) == 0 or len(website_entry.get().strip()) == 0:
        messagebox.showinfo(title="Error", message="Fill in all the entries please")
        return

    is_sure = messagebox.askokcancel(title=website_entry.get(),
                                     message=f"Email/Username: {username_entry.get()}\nPassword: {password_entry.get()}\nIs it okay to save?")

    if not is_sure:
        return

    try:
        with open("accounts.txt", mode="a") as file:
            file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
    except FileNotFoundError:
        with open("accounts.txt", mode="w") as file:
            file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
    website_entry.delete(0, END)
    pyperclip.copy(password_entry.get())  # copy the password to the clipboard
    password_entry.delete(0, END)
    messagebox.showinfo(title="Success", message="The login information was successfully saved")


# ==================================================================
# creating a function to generate random password
# ==================================================================


def generate_password():
    global password_entry
    password_entry.delete(0, END)
    password = [chr(randint(65, 122)) for i in range(randint(4, 7))]
    password += [chr(randint(33, 37)) for i in range(randint(2, 5))]
    password += [chr(randint(48, 57)) for i in range(randint(3, 6))]
    shuffle(password)
    password_entry.insert(0, "".join(password))


# ==================================================================
# creating a canvas with the width and the height of logo.png image
# ==================================================================

canvas = Canvas(width=200, height=200)

# ==================================================================
# creating an image using logo.png file
# ==================================================================

image = PhotoImage(file="logo.png")

# ==================================================================
# including that image into our canvas
# ==================================================================

canvas.create_image(100, 100, image=image)

# ==================================================================
# creating labels to display texts
# ==================================================================

website_label = Label(text="Website: ")
username_label = Label(text="Email/Username: ")
password_label = Label(text="Password: ")

# ==================================================================
# creating entries to take input from the user
# ==================================================================

website_entry = Entry(width=51)
username_entry = Entry(width=51)
password_entry = Entry(width=33)

# ==================================================================
# creating buttons to let the user save or generate password
# ==================================================================

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
add_button = Button(text="Add", width=43, command=add_user)

# ==================================================================
# placing all widgets using grid
# ==================================================================

website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1, columnspan=2)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=1)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

canvas.grid(row=0, column=1)

# ==================================================================

# set the focus to website widget so that user can start typing from there
# insert the text into email field so that user already has his most
#  commonly used email entered
# ==================================================================

website_entry.focus()
username_entry.insert(0, "quluzadea73@gmail.com")

# ==================================================================


window.mainloop()
