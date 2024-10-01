import tkinter as tk
from tkinter import messagebox
from functools import partial


def login(userName):
    if userName.get() != "พีสะเดิด":
        # warning
        messagebox.showwarning(
            "แกไม่มีสิทธิ!!!", "คุณไม่ใช่พีสะเดิด คุณไม่มีสิทธิจี่หอย")
    else:
        # Go to play page
        page2()


def page2():
    top.destroy()
    import game


top = tk.Tk()
top.title("Jeehoy LOGIN")
top.geometry("900x500")
userName = tk.StringVar()
tk.Label(top, text="UserName").place(x=400, y=170)
tk.Entry(top, textvariable=userName).place(x=340, y=200)
login = partial(login, userName)
tk.Button(top, text="Login", command=login).place(x=400, y=235)

top.mainloop()
