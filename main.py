import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import secrets
import string
import pyperclip
# ~~~~~~~~~ PASSWORD GENERATOR ~~~~~~~~~ #
def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for i in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, secure_password)
    pyperclip.copy(secure_password)

# ~~~~~~~~~ SAVE EMAIL/PASSWORD ~~~~~~~~~ #
def save():

    account = account_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(account) == 0 or len(password) == 0:
        messagebox.showinfo(title="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=account, message=f"Here are the details entered:"
                                                  f" \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{account}: {email} | {password}\n")
                account_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# ~~~~~~~~~ GUI ~~~~~~~~~ #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)
window.columnconfigure(0, weight=1)

# CANVAS
canvas = tk.Canvas(height=250, width=200)
canvas.grid(row=0, column=0)

# LOGO
original_image = Image.open("lock-logo.png")
resized_image = original_image.resize((200,200), Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_image)
canvas.create_image(100,150,image=logo_img)

# LABELS
account_label = tk.Label(text="Account:")
account_label.grid(row=1, column=0, sticky="w")
email_label = tk.Label(text="Email / Username:")
email_label.grid(row=3, column=0, sticky="w")
password_label = tk.Label(text="Password:")
password_label.grid(row=5, column=0, sticky="w")

# ENTRIES
account_entry = tk.Entry(width=35)
account_entry.grid(row=2, column=0, sticky="w")
account_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(row=4, column=0, sticky="w")
email_entry.insert(0,"sample@gmail.com")
password_entry = tk.Entry(width=21)
password_entry.grid(row=6, column=0, sticky="w")

# BUTTONS
generate_password_button = tk.Button(text="Generate Password", command=lambda: generate_password(12))
generate_password_button.grid(row=6, column=0, sticky="e")
add_password_button = tk.Button(text="Add", width=33, command=save)
add_password_button.grid(row=7, column=0)


window.mainloop()