""" Basic tkinter gui template """
import tkinter

from tkinter import scrolledtext
from button_func import *

# make a window
window = tkinter.Tk()

# set the window size (sets it by pixels (w, h))
window.geometry('600x700')

# give window a title
window.title("Assign01")

# change the background color of window
window.configure(background = 'black')

# ----------------------------------------------------------------------------

readyList = []
blockedList = []
endList = []

currentProcess = generateProcess(-1)

# ----------------------------------------------------------------------------

# make labels
running_lbl = tkinter.Label(
    window, text = 'Running', fg = 'white', bg = 'black', 
    font = ("Arial Bold", 10))
readyList_lbl = tkinter.Label(
    window, text = 'Ready List', fg = 'white', bg = 'black',
    font = ("Arial Bold", 10))
blockedList_lbl = tkinter.Label(
    window, text = 'Blocked List',fg = 'white', bg = 'black',
    font = ("Arial Bold", 10))
termList_lbl = tkinter.Label(
    window, text = 'Terminated List',fg = 'white', bg = 'black',
    font = ("Arial Bold", 10))


# position labels  
# .place is absolute (will not be moved by anything once placed)
running_lbl.place(x = 5, y = 0)
readyList_lbl.place(x = 5, y = 100)
blockedList_lbl.place(x= 5, y = 315)
termList_lbl.place(x = 5, y = 515)

# ----------------------------------------------------------------------------

# make text boxes
running_box = tkinter.Entry(window, width = 60, fg = 'white', bg = 'black')
ready_box = scrolledtext.ScrolledText(window, width = 43, height = 8, 
    fg = 'white', bg = 'black')
blocked_box = scrolledtext.ScrolledText(window, width = 43, height = 8,
    fg = 'white', bg = 'black')
terminated_box = scrolledtext.ScrolledText(window, width = 43, height = 8,
    fg = 'white', bg = 'black')

# position boxes
running_box.place(x = 5, y = 25)
ready_box.place(x = 5, y = 125)
blocked_box.place(x = 5, y = 350)
terminated_box.place(x = 5, y = 550)

# running_box.insert(0, "testing...") # testing input method

# ----------------------------------------------------------------------------

# make buttons
addProcess_btn = tkinter.Button(window, text = 'Add Process', 
    command = lambda : [onAddProcess
    (ready_box, readyList, running_box, currentProcess)])
    
block_btn = tkinter.Button(window, text = 'Block')
timeSlice_btn = tkinter.Button(window, text = 'Time Slice')
term_btn = tkinter.Button(window, text = 'Terminate')
send_btn = tkinter.Button(window, text = 'Send To Ready')

# position buttons
addProcess_btn.place(x = 140, y = 55)
block_btn.place(x = 400, y = 5)
timeSlice_btn.place(x = 400, y = 35)
term_btn.place(x = 400, y = 65)
send_btn.place(x = 400, y = 400)

# ----------------------------------------------------------------------------

# actually brings up the window
window.mainloop()