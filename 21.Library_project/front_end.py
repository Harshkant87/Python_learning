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
import back_end

def view_command():
    listbox_window.delete(0, END)
    for row in back_end.view():
        listbox_window.insert(END, row)

def search_command():
    listbox_window.delete(0, END)
    for row in back_end.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox_window.insert(END, row)

def add_command():
    listbox_window.delete(0, END)
    back_end.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox_window.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


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

listbox_window = Listbox(window, height = 6, width = 35)
listbox_window.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scrl_bar = Scrollbar(window)
scrl_bar.grid(row = 2, column = 2, rowspan = 6)
listbox_window.configure(yscrollcommand = scrl_bar.set)
scrl_bar.configure(command = listbox_window.yview)

button1 = Button(window, text = "View All", width = 12, command = view_command)
button1.grid(row = 2, column = 3)

button2 = Button(window, text = "Search Entry", width = 12, command = search_command)
button2.grid(row = 3, column = 3)

button3 = Button(window, text = "Add Entry", width = 12, command = add_command)
button3.grid(row = 4, column = 3)

button4 = Button(window, text = "Update", width = 12)
button4.grid(row = 5, column = 3)

button5 = Button(window, text = "Delete", width = 12)
button5.grid(row = 6, column = 3)

button6 = Button(window, text = "Close", width = 12)
button6.grid(row = 7, column = 3)

window.mainloop()
