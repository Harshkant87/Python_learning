from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)

b1 = Button(window, text = "Execute", command = km_to_miles) # button
# b1.pack() # place this widget
b1.grid(row = 0, column = 1)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 2) #Another method to place widget with specific location

t1 = Text(window, height= 1, width = 20)
t1.grid(row = 2, column = 1)

window.mainloop()

