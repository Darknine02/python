#layout mabagenebt pack e grid
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')

#padding distanza dell'elemento dal container, ipadding distanza tra il bordo dal contenuto 
#il pack aggiunge i container in verticale. il comando fill riempie per la lunghezza di x. 
# Expend true assegna più spazio, il disponibile nella finestra. 
# side left li mette in orizzontale
label1 = Label(root, text="Laber 1", background="green", foreground='white')
label1.pack(padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill=BOTH, side=LEFT)

label2 = Label(root, text="Laber 2", background="red", foreground='white')
label2.pack(padx=10, pady=10, ipadx=10, ipady=10, fill=X, side=LEFT)
root.mainloop()

root2 = Tk()
root2.geometry('600x400')
#grid crea una griglia 
root2.columnconfigure(0, weight=1)
root2.columnconfigure(1, weight=2)

frame1 = Frame(root2, background='red', height=200, width=200)
frame2 = Frame(root2, background='purple', height=200, width=200)
frame3 = Frame(root2, background='cyan', height=200, width=200)
frame4 = Frame(root2, background='yellow', height=200, width=200)

frame1.grid(column=0, row=0, rowspan=2)
frame2.grid(column=1, row=0)
#frame3.grid(column=0, row=1)
frame4.grid(column=1, row=1)
root2.mainloop()