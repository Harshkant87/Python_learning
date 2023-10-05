'''
A Program that stores following information of book:

Tiltle,
Author,
Year,
ISBN

A user can:

1) View all records
2) Search an entry
3) Add entry
4) Update entry
5) Delete
6) Close

'''

from tkinter import *

window = Tk()

title_label = Label(window, text = "Title")
title_label.grid(row = 0, column = 0)

author_label = Label(window, text = "Author")
author_label.grid(row = 0, column = 2)

year_label = Label(window, text = "Year")
year_label.grid(row = 1, column = 0)

isbn_label = Label(window, text = "ISBN")
isbn_label.grid(row = 1, column = 2)

title_text = StringVar()
title_entry = Entry(window, textvariable = title_text)
title_entry.grid(row = 0, column = 1)

author_text = StringVar()
author_entry = Entry(window, textvariable = author_text)
author_entry.grid(row = 0, column = 3)

year_text = StringVar()
year_entry = Entry(window, textvariable = year_text)
year_entry.grid(row = 1, column = 1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable = isbn_text)
isbn_entry.grid(row = 1, column = 3)


window.mainloop()
