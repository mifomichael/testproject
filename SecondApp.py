import tkinter as tk
from PIL import ImageTk
from PIL import Image
from tkinter import StringVar
from tkinter import Label
from tkinter import ttk
from tkinter import IntVar
from tkinter import Radiobutton
from tkinter import filedialog
from tkinter import scrolledtext 


window = tk.Tk()
# set window size
window.geometry("800x400")

#set window color
window.configure(bg='#1d2e33')

#___logo___
img = tk.PhotoImage(file="Logo2.png") 
panel = tk.Label(window, image = img, borderwidth=0, highlightthickness=0)
panel.grid (row = 0, column = 0)

#___Text Title____
var = StringVar()
label = Label( window, textvariable=var, bg='#1d2e33', fg ="yellow", padx= 100,  )
var.set("Splitting Application")
label.grid(row = 0, column = 1)
label.config(font=("Georgia", 25))

#---- Radio Button---

var1=StringVar()
l = tk.Label(window, bg='#1d2e33', fg ="yellow", width=30, text=' ')
l.grid(column = 0, row = 3, sticky='nw')
 
def sel():
    l.config(text='you have selected ' + var1.get())

style = ttk.Style(window)

style.theme_use('alt')

common_bg = '#1d2e33'  
common_fg = 'yellow' 

rad_button = ttk.Radiobutton(window, text='CSV(comma)', value='csv', variable= var1)
rad_button.grid(row=1, column= 0,sticky='nw')
rad_button2 = ttk.Radiobutton(window, text='Text(space)',value='text', variable = var1)
rad_button2.grid(row = 2, column = 0, sticky='nw')

style_name = rad_button.winfo_class()
style.configure(style_name, foreground=common_fg, background=common_bg, indicatorcolor=common_bg)

style.map(style_name,
          foreground = [('disabled', common_fg),
                      ('pressed', common_fg),
                      ('active', common_fg)],
          background = [('disabled', common_bg),
                      ('pressed', '!focus', common_bg),
                      ('active', common_bg)],
          indicatorcolor=[('selected', common_bg),
                          ('pressed', common_bg)]

          )

#---Slicing button----

def file_opener():
   text_area.delete(1.0, tk.END)
   input = filedialog.askopenfile(initialdir="Coding")
  
   #file1 = input.name
   #content = open(file1)
   #textcontent = content.read()
   #alllines = textcontent.splitlines()
   #print( len(alllines))
   #print(alllines[0])

   #for a in alllines:
      # print(a)

   print(input)

   for i in input:

        if var1.get() == "csv":
            x = i.split(",")

            for b in x:
                c = b.strip()
                print(c)
                text_area.insert(tk.END, c+"\n")

        elif var1.get() == "text":
            x = i.split("\t")

            for b in x:
                c = b.strip()
                print(c)
                text_area.insert(tk.END, c+"\n")
                
                
                
# Button label
x = tk.Button(window, text ='Select a file', command = lambda:file_opener())
x.grid(row=5 , column=0)



#---text window---

text_area = scrolledtext.ScrolledText(window,  
                                      wrap = tk.WORD,  
                                      width = 40,  
                                      height = 7,  
                                      font = ("Times New Roman", 
                                              12)) 
  
text_area.grid(row = 6, column = 1, pady = 10, padx = 10) 

window.mainloop()