
    # Error 1.0: pwede ka mag enter ng mag enter
    # Done 1.1: Hindi naka centre
    # Error 1.2: Di nag aadjust yung text field based sa lenght ng sinubmit

from tkinter import *

def submit():
    name = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"Hello {name}, I am Uzziel ")

def clear():
    entry.delete(0, END)

window = Tk()
window.title('Activity 1')

# Set the initial size and center the window
window.geometry('300x300')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 300) // 2
y = (screen_height - 300) // 2
window.geometry(f'300x300+{x}+{y}')

label = Label(window, text="What is your name?")
entry = Entry(window)
submit_button = Button(window, text="Submit", command=submit)
clear_button = Button(window, text="Clear", command=clear)

# Using the grid geometry manager to center the label and entry
label.grid(row=0, column=0, pady=10, sticky='nsew')
entry.grid(row=1, column=0, pady=5, padx=10, sticky='ew')
submit_button.grid(row=2, column=0, pady=10)
clear_button.grid(row=3, column=0, pady=10)

# Column and row configurations to make the label expandable
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

window.mainloop()
