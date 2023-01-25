#Cosa sono, crearne uno e multipli, padding, background, inserire widget
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')

#I frame sono come i div di html, si possono creare e inserire dentro oggetti
frame1 = Frame(root, background="red", padx=10, pady=50, height=100, width=200)
frame2 = Frame(root, background="yellow", padx=10, pady=50, height=100, width=200)
frame3 = Frame(root, background="green", padx=10, pady=50, height=100, width=200)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

#widget da inserire devono avere il nome del frame
Button1 = Button(frame1, text="Ciao").pack()
Button2 = Button(frame2, text="Hello").pack()
Button3 = Button(frame3, text="HI").pack()
root.mainloop()