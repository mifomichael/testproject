import tkinter as tk
from tkinter import filedialog
base = tk.Tk()
# Create a canvas
base.geometry('150x150')
# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)
# Button label
x = tk.Button(base, text ='Select a .txt/.csv file', command = lambda:file_opener())
x.pack()
base.mainloop()