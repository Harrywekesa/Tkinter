from tkinter import *

app = Tk()

myframe = Frame()
myframe.grid()

label_top_left = Label(myframe, text = "I am at (1,1)")
label_top_left.grid(row = 1, column = 1)

label_bottom_left = Label(myframe, text = "I am at (2,1)")
label_bottom_left.grid(row = 2, column = 1)

button_bottom_right = Button(myframe, text = "I am at (3, 2")
button_bottom_right.grid(row = 3, column = 2)

app.mainloop()