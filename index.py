import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# ส่วนของwindowด้านบนและขนาดของwindow
root = Tk()
root.title('jEeHoY')
root.geometry("900x500")

# รูปพื้นหลัง
image = Image.open("ff.png")
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=10, y=0, relwidth=1, relheight=1)


def login():
    root.destroy()
    import login


# ส่วนของข้อความjee hoy และปุ่มกดstrat jeehoy
Text = tk.Label(root, text='jEeHoY', width=10, height=2, font=("Arial", 70))
Text.pack()
Button = tk.Button(root, command=login, text="Start jEeHoY",
                   width=12, height=1, font=("Arial", 30))
Button.pack()


root.mainloop()
