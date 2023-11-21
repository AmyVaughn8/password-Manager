import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=300, width=300)
canvas.pack()

original_image = Image.open("lock-logo.png")
resized_image = original_image.resize((150,150), Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_image)
canvas.create_image(150,150,image=logo_img)

window.mainloop()