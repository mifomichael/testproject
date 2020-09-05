from tkinter import *
import tkinter.colorchooser
from tkinter.colorchooser import askcolor

win = Tk()

# Open a color dialog box
def openColorDialog():
     win.buttoncolor.configure(bg=askcolor()[1])


win.buttoncolor = Button(win,text="Choose Color",command=openColorDialog)
win.buttoncolor.grid(row = 2, column = 2, sticky = W)

win.mainloop()