from tkinter import *

app = Tk()
app.geometry("200x50")

#Create side by side frames
frameleft = Frame(bd = 3, relief = SUNKEN)
frameleft.place(relx = 0, relwidth = 0.5, relheight = 1) #Relx provides a relative x placement, that takes a value from 0 to 1 to representa fraction of the windows width

frameright = Frame(bd = 3, relief = SUNKEN)
frameright.place(relx = 0.7, relwidth = 0.3)

leftlabel = Label(frameleft, text = "I have been framed")
leftlabel.pack()

rightlabel = Label(frameright, text = "I have been framed")
rightlabel.pack()

app.mainloop()