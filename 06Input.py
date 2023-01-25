#Creare esempio di login
from tkinter import *
from tkinter import ttk
def login():
    print(email_entry.get(), password_entry.get())

root = Tk()
root.geometry('600x400')

#Campo di entrata per email
label_email = Label(root, text='Email')
label_email.pack(padx=5, pady=5)

email = StringVar()
email_entry = ttk.Entry(root, textvariable=email)
email_entry.pack(padx=5, pady=5)
email_entry.focus()

#Campo di entrata per password
label_pass = Label(root, text='Password')
label_pass.pack(padx=5, pady=5)

password = StringVar()
password_entry = ttk.Entry(root, textvariable=password, show="*")
password_entry.pack(padx=5, pady=5)

button = ttk.Button(root, text="Login", command=login).pack()

root.mainloop()