import tkinter
from tkinter import filedialog

def write_File (text_File):

    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    file = open(window.filename,"a")
    user_Input = text_File.get("1.0", "end")
    file.write(user_Input)
    file.close()

window = tkinter.Tk()


the_input = tkinter.Text(window)
the_input.grid(row=1, column=1)

tkinter.Button(window, text = "Send to file:", command = lambda: write_File(the_input)).grid(row=10, column=1)

window.mainloop()