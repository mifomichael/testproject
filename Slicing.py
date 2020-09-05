import tkinter as tk
from tkinter import filedialog
base = tk.Tk()
# Create a canvas
base.geometry('150x150')
# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="Coding")
  
   file1 = input.name
   content = open(file1)
   textcontent = content.read()
   alllines = textcontent.splitlines()
   print( len(alllines))
   print(alllines[0])

   for a in alllines:
       print(a)

   print(input)

   for i in input:
      x = i.split("\t")
      for b in x:
         c = b.strip()
         print(c)
# Button label
x = tk.Button(base, text ='Select a .txt/.csv file', command = lambda:file_opener())
x.pack()
base.mainloop()