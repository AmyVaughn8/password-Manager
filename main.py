import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = tk.Canvas(height=300, width=200)
canvas.grid(row=0, column=1)

# image
original_image = Image.open("lock-logo.png")
resized_image = original_image.resize((150,150), Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_image)
canvas.create_image(150,150,image=logo_img)

# labels
website_label = tk.Label(text="Website")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email / Username")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0)

# entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()