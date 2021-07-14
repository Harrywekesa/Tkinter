from tkinter import *

def recalc():
    cel_temp = entry_cel.get() #get tempereature in celcius from an entry
    try: #Calculate converted temperature and place it in a label
        far_Temp = float(cel_temp) * 9/5 + 32
        far_Temp = round(far_Temp, 3) #Round off into 3 decimal places
        result_far.config(text = far_Temp)
    except ValueError: #User entered non-numeric values
        result_far.config(text = "Invalid input")
        
app = Tk()
app.title("Temperature converter")

#Creating a frame
frame = Frame()
frame.grid(padx = 5, pady = 5) #Pad top and left of the grid 5 pixels before grid

#Create and label labels
label_cel = Label(frame, text = "Celcius temperature")
label_cel.grid(row = 1, column = 1, sticky = S+E)
label_far = Label(frame, text = "Farenheit temperatu")
label_far.grid(row = 2, column = 1, sticky = S+E)

#Creating user entery fields
entry_cel = Entry(frame, width = 7)
entry_cel.grid(row = 1, column = 2)
entry_cel.insert(0, 0)

#Create and add label for text calculation results
result_far = Label(frame)
result_far.grid(row = 2, column = 2)

#create and add recalculate button
btn_recalculate = Button(frame, text = "Recalculate", command  = recalc)
btn_recalculate.grid(row = 1, column = 3, rowspan = 2)

recalc() #Fill in default temperature conversion
mainloop() #Start the application
