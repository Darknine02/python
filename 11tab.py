#notebook
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')

#creare notebook
notebook = ttk.Notebook(root)
notebook.pack(padx=10, fill=BOTH, expand=True)

#creare contenitore
frame1 = ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill=BOTH, expand=True)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame2.pack(fill=BOTH, expand=True)

#assocciare ogni frame ad un menu
notebook.add(frame1, text='tab1')
notebook.add(frame2, text='tab2')

label1 = Label(frame1, text='Ciao')
label1.pack()
label2 = Label(frame2, text='Buongiorno')
label2.pack()
root.mainloop()