import tkinter as tk
import smtplib

window = tk.Tk()
window.title("Greetings _____")
window.geometry("400x400")



#----Functions----
def email_generator():
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()

    
    #sender = getpass.getpass("test4python123@gmail.com")
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

#----Label----
label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your email? ")
label2.grid(column=0, row=1)

#----Entries----
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

#----Button----
button1 = tk.Button(text="CLICK ME!", command=phrase_display)
button1.grid(column=0, row=2)

window.mainloop()