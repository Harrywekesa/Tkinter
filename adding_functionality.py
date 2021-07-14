from tkinter import *

app = Tk()
def increment_button():
    new_number = 1 + Button.cget("text")
    Buttonnew_number = 1 + Button.config(text = new_number)
    
btn1 = Button(text = 1 , command = increment_button)
btn1.pack()

mainloop()