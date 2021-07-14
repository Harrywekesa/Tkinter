from tkinter import *

app = Tk()

entry1 = Entry()
entry1.pack()
entry1.insert(0, "This is an entry")

entry2 = Entry()
entry2.pack()

mytext = entry1.get() #get text from entry 1
entry2.insert(0, mytext)
entry2.insert(8, "also") #Adding text at the middle of my sentence

mainloop()
