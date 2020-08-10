from tkinter import filedialog
import tkinter as tk

window = tk.Tk()

def delete():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    print (window.filename)
    os.remove(window.filename)

btn = tk.Button(window, text = 'Delete File', command = lambda : delete()) 
btn.grid(column=0,row=6)

window.mainloop()