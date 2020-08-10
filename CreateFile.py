from tkinter import *
root = Tk()

def clicked():
    Input = entry1.get()
    FileName = str("filepath" + Input + ".txt")
    TextFile = open(FileName,"w")

entry1 = Entry(root)
button1 = Button(root,text="Press to create text file", command = clicked)
entry1.pack()
button1.pack()

root.mainloop()