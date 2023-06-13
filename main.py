from tkinter import *
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=5)

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)

window.mainloop()
