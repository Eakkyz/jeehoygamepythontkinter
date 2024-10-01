from tkinter import *
number = 0

root = Tk()
top = Toplevel()  # สร้างหน้าต่างใหม่ขึ้นมา
top.geometry("900x500")
root.geometry('500x400')
top.title("jEeHoy End")


def stop():
    root.deiconify()  # ทำการแสดงหน้าต่างหลัก หากตรงตามเงื่อนไข
    top.destroy()  # ปิดหน้าต่างที่สร้างขึ้นมาใหม่ หากตรงตามเงื่อนไข


def restart():
    top.destroy()
    root.destroy()
    import game


label = Label(top, text='คุณจี่หอยเก่งมาก', fg="red", font=100)
label1 = Label(top, text='SCORE :  ', fg="green", font=10)
button1 = Button(top, text="จี่หอยต่อ", font=200, command=restart)
button2 = Button(top, text='พอเเล้วนะ', font=200, command=stop)
label2 = Label(root, text="jEeHoy Success jaa", font=200)

label.pack()
label1.pack()
button1.place(x=250, y=100)
button2.place(x=550, y=100)
label2.pack()

root.withdraw()  # ทำการซ่อนหน้าต่างหลัก
root.mainloop()
