from tkinter import *
import tk_file_dialogue

app = Tk()
frame =  Frame()
frame.pack()

def openfile():
    typelist = [("Python scripts", ".py"), ("Text file", ".txt")]
    filename = tk_file_dialogue.askopenfilename(filetypes = typelist)
    labelfile.config(text = filename)
    
#Blank label to hold the names of the chosen files
labelfile = Label(frame)
labelfile.pack()

#Button to click on for open "file" dialog
buttonOpen = Button(frame, text = "Choose a file...", command = openfile)
buttonOpen.pack()

mainloop()