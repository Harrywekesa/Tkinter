# Gui setup for complex applications
from tkinter import *

#Define the gui application
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
#Creating application window
window = Tk()
window.geometry("400x200") #Default window size
myapp = App(window)
myapp.master.title("Serious stuffs")
myapp.pack()
myapp.mainloop() #Sart the app