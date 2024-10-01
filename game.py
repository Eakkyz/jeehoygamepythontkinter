import tkinter as tk
import random
from tkinter import *
from PIL import ImageTk, Image
import os

number = 0
luck = 0
point = 0

i1 = True
i2 = True
i3 = True
i4 = True
i5 = True
i6 = True
i7 = True
i8 = True
i9 = True
i10 = True
i11 = True
i12 = True
i13 = True
i14 = True
i15 = True
i16 = True
i17 = True
i18 = True
i19 = True
i20 = True
i21 = True



master = tk.Tk()
master.title('Hello Wor`ld')
master.geometry("900x500")

img =  Image.open("sea.png")
photo = ImageTk.PhotoImage(img)

img2 =  Image.open("sea2.png")
photo2 = ImageTk.PhotoImage(img2)

def ClickButton():
    global number
    global i1
    ShowInfo["text"] = "You JeeHoy " + str(number) + " times."
    luck = random.randint(1,21)
    if(luck==1):
        lb1.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==2):
        lb2.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==3):
        lb3.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==4):
        lb4.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==5):
        lb5.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==6):
        lb6.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==7):
        lb7.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==8):
        lb8.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==9):
        lb9.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==10):
        lb10.config(image=photo2)
        i10 = True
        check1(i1)
    elif(luck==11):
        lb11.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==12):
        lb12.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==13):
        lb13.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==14):
        lb14.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==15):
        lb15.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==16):
        lb16.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==17):
        lb17.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==18):
        lb18.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==19):
        lb19.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==20):
        lb20.config(image=photo2)
        i1 = True
        check1(i1)
    elif(luck==21):
        lb21.config(image=photo2)
        i1 = True
        check1(i1)

def check1(i1):
    global number
    # ShowInfo["text"] = "You JeeHoy " + str(number) + " times."
    if(i1):
        number += 1
        i1 = False
    else:
        number -= 1


def Next():
    global number
    
    if not (os.path.exists("score.txt")):
        f = open("score.txt", "x")
        f.write(str(number))
    else:
        f = open("score.txt", "w")
        f.write(str(number))
    master.destroy()
    import score


lb1 = tk.Button(master, image=photo, command=ClickButton)
lb1.place(x = 30, y = 150)

lb2 = tk.Button(master, image=photo, command=ClickButton)
lb2.place(x = 30, y = 250)

lb3 = tk.Button(master, image=photo, command=ClickButton)
lb3.place(x = 30, y = 350)

lb4 = tk.Button(master, image=photo, command=ClickButton)
lb4.place(x = 115, y = 250)

lb5 = tk.Button(master, image=photo, command=ClickButton)
lb5.place(x = 200, y = 150)

lb6 = tk.Button(master, image=photo, command=ClickButton)
lb6.place(x = 200, y = 250)

lb7 = tk.Button(master, image=photo, command=ClickButton)
lb7.place(x = 200, y = 350)

lb8 = tk.Button(master, image=photo, command=ClickButton)
lb8.place(x = 310, y = 150)

lb9 = tk.Button(master, image=photo, command=ClickButton)
lb9.place(x = 310, y = 250)

lb10 = tk.Button(master, image=photo, command=ClickButton)
lb10.place(x = 310, y = 350)

lb11 = tk.Button(master, image=photo, command=ClickButton)
lb11.place(x = 400, y = 150)

lb12 = tk.Button(master, image=photo, command=ClickButton)
lb12.place(x = 400, y = 350)

lb13 = tk.Button(master, image=photo, command=ClickButton)
lb13.place(x = 490, y = 150)

lb14 = tk.Button(master, image=photo, command=ClickButton)
lb14.place(x = 490, y = 250)

lb15 = tk.Button(master, image=photo, command=ClickButton)
lb15.place(x = 490, y = 350)

lb16 = tk.Button(master, image=photo, command=ClickButton)
lb16.place(x = 600, y = 150)

lb17 = tk.Button(master, image=photo, command=ClickButton)
lb17.place(x = 600, y = 250)

lb18 = tk.Button(master, image=photo, command=ClickButton)
lb18.place(x = 690, y = 250)

lb19 = tk.Button(master, image=photo, command=ClickButton)
lb19.place(x = 690, y = 350)

lb20 = tk.Button(master, image=photo, command=ClickButton)
lb20.place(x = 780, y = 250)

lb21 = tk.Button(master, image=photo, command=ClickButton)
lb21.place(x = 780, y = 150)

lb22 = tk.Button(master, command=Next, text="Next" )
lb22.place(x = 800, y = 100)

ShowInfo = Label(master, text="Jeehoy Farm", font=("Arial, 20"), fg="purple")
ShowInfo.place(x = 100, y = 100)

ShowInfo.pack()

master.mainloop()