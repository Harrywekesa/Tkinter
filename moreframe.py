from tkinter import *

app = Tk()

myframe = Frame()
myframe.pack()

labeltext1 = Label(myframe, text = "Top bar", bg = "Blue", fg = "Black", font = "Arial")
labeltext1.pack(fill = X)

labeltext2 = Label(myframe, text = "Left", bg = "yellow")
labeltext2.pack(side = LEFT) #Place label to the left of the next widget

labeltext3 = Label(myframe, text = "Midground", bg = "Orange",)
labeltext3.pack(side = LEFT) #Place label to the left of the next widget

labeltext4 = Label(myframe, text = "Right", bg = "Green", fg = "Red",)
labeltext4.pack()

app.mainloop()
