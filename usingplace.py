from tkinter import *

app = Tk()
app.geometry("200x200")

frame1 = Frame()
frame1.pack()

btn1 = Button(frame1, text = " I am at (100, 150)")
btn1.pack()
btn1.place(x = 100, y = 150)

btn2 = Button(frame1, text = "Button2 at (0, 0)")
btn2.pack()
btn2.place(x = 0, y = 0, width = 100, height = 50)

app.mainloop()