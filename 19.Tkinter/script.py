from tkinter import *

window = Tk()

b1 = Button(window, text = "Execute") # button
# b1.pack() # place this widget
b1.grid(row = 0, column = 1)

e1 = Entry(window)
e1.grid(row = 0, column = 2) #Another method to place widget with specific location

t1 = Text(window, height= 1, width = 20)
t1.grid(row = 2, column = 1)

window.mainloop()

