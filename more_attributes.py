from tkinter import *

app = Tk()

myframe = Frame()
myframe.grid()

label_top_left = Label(myframe, text = "I am at (1, 1)", bd = "3", relief = SUNKEN)
label_top_left.grid(row = 1, column = 1, padx = 100, pady = 30)

label_bottom_left = Label(myframe, text = "I am at (2, 1)", bd = "3",relief = SUNKEN)
label_bottom_left.grid(row = 2, column = 1, sticky = E) # Sticky e says that the label should stick east if there is extra horizontal space

button_right = Button(myframe, text = "I span two rows", height = 5)
button_right.grid(row = 1, column = 2, rowspan = 2)

app.mainloop()
