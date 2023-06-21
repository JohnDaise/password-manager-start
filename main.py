from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def search_website():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            site = data[website]
            # print(data[website])
    except FileNotFoundError:
        # write the file
        messagebox.showinfo(title="File Not Found", message="Data file not found \n")
    except KeyError:
        messagebox.showinfo(title=website, message=f"Email/Password for {website} not found \n")
    else:
        email = site['email']
        password = site['password']
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password} \n")


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

    # print(f"Your password is: {generated_password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_entry_data():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Wait a sec...", message="Please make sure you enter website and password")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        #     new_file_name_path = "./data.json"
        try:
            with open("data.json", "r") as write_file:
                # Read
                data = json.load(write_file)
                # Update
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as write_file:
                json.dump(new_data, write_file, indent=4)
                # data = json.load(write_file)
        else:
            data.update(new_data)

            with open("data.json", "w") as write_file:
                # Saving Updated Data
                json.dump(data, write_file, indent=4)
        finally:
            clear_entry_data()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)

# Lock Logo
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", fg="black", bg=WHITE)
website_label.grid(column=0, row=1, padx=6, pady=6)

email_username_label = Label(text="Email/Username:", fg="black", bg=WHITE)
email_username_label.grid(column=0, row=2, padx=6, pady=6)

password_label = Label(text="Password:", fg="black", bg=WHITE)
password_label.grid(column=0, row=3, padx=6, pady=6)

# Entries

website_entry = Entry(width=20, highlightthickness=0, fg="black", bg=WHITE)
website_entry.grid(column=1, row=1)


email_username_entry = Entry(width=35, highlightthickness=0, fg="black", bg=WHITE)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "name@email.com")


password_entry = Entry(width=20, highlightthickness=0, fg="black", bg=WHITE)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=10, padx=5, pady=2, bg=WHITE, borderwidth=0,
                                  highlightthickness=0, command=search_website)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", width=10, padx=5, pady=2, bg=WHITE, borderwidth=0,
                                  highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, padx=2, pady=2, bg=WHITE, borderwidth=0, highlightthickness=0,
                    command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
