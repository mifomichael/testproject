import tkinter as tk
import smtplib
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os
import tkinter.ttk as ttk
import tkinter.colorchooser
from tkinter.colorchooser import askcolor

window = tk.Tk()
window.title("Greetings _____")
window.geometry("400x400")





#----Functions Email----
def email_generator():
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()

    
    sender = "test4python123@gmail.com"
    password = "edzdffghktdwrfus"
    smtp_object.login(sender,password)


    email = str(entry1.get())
    from_address = sender
    to_address = email
    subject = ("Hello")
    message = ("This is your button email!")
    msg = "Subject: "+subject+'\n' +message 

    smtp_object.sendmail(from_address,to_address,msg)


    return "Email sent to " + email

def phrase_display():
    greeting = email_generator()

    # This creates a text field
    greeting_display = tk.Text(master=window, heigh=10, width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)

#--file open button---

def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)

#----Label----
label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your email? ")
label2.grid(column=0, row=1)

#----Entries----
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

#----Button----
#--email send
button1 = tk.Button(text="Send Email", command=phrase_display)
button1.grid(column=0, row=2)

#---file open---
button2 = tk.Button(text="Open File", command=file_opener)
button2.grid(column=0, row=3)


#--save file directory ----
def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    Input3 = entry3.get()
    FileName3 = str(Input3 + ".txt")
    files = asksaveasfile(filetypes = files, defaultextension = files, initialfile = FileName3) 
  
btn = tk.Button(window, text = 'Save File', command = lambda : save()) 
btn.grid(column=0,row=5)
entry3 = tk.Entry()
entry3.grid(column=1, row=5)

#---Delete File ---
def delete():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    print (window.filename)
    os.remove(window.filename)

btn = tk.Button(window, text = 'Delete File', command = lambda : delete()) 
btn.grid(column=0,row=6)


#---write file----


def write_File (text_File):

    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    file = open(window.filename,"a")
    user_Input = text_File.get("1.0", "end")
    file.write(user_Input)
    file.close()

the_input = tk.Text(window, height= 5, width = 30)
the_input.grid(row=7, column=1)

tk.Button(window, text = "Send to file:", command = lambda: write_File(the_input)).grid(column=0,row=7)


#---scroll bar---
scrollb = ttk.Scrollbar(window, command=the_input.yview)
scrollb.grid(row=7, column=2, sticky='nsew')
the_input['yscrollcommand'] = scrollb.set
style = ttk.Style()
style.theme_use('clam')

#----Color Chooser----

def openColorDialog():
     window.buttoncolor.configure(bg=askcolor()[1])


window.buttoncolor = tk.Button(window,text="Choose Color",command=openColorDialog)
window.buttoncolor.grid(row = 8, column = 0)

window.mainloop()

