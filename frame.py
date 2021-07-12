from tkinter import *

window = Tk()
window.title("Anotherone simple from me")
window.geometry("250x100")

myframe = Frame()
myframe.pack()

labeltext = Label(myframe, text = "I have been framed!", bg = "red", fg = "yellow", font = "Arial") #myframe assigns the label to the frame
labeltext.pack()

window.mainloop()