#Scrollbar applicata a listbox, scrolltext
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext 
from turtle import width

root = Tk()
root.geometry('600x400')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#creo listbox
linguaggi = ('Javascript', 'Java','c','c++','python', 'php', 'ruby', 'GO', 'Javascript', 'Java','c','c++','python', 'php', 'ruby', 'GO', 'Javascript', 'Java','c','c++','python', 'php', 'ruby', 'GO', 'Javascript', 'Java','c','c++','python', 'php', 'ruby', 'GO')
linguaggio_selezionato = StringVar(value=linguaggi)

listbox = Listbox(root, listvariable=linguaggio_selezionato, height=6, selectmode='extended')
listbox.grid(column=0, row=0, sticky='nwes')

#creo scroolbar verticale e si connette al nostro widget listbox nella sua yview. abbiamo messo a schermo la scrollbar
scrollbar = ttk.Scrollbar(root, orient='vertical', command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

#collegato listbox con scrollbar
listbox['yscrollcommand'] = scrollbar.set

root.mainloop()




#crea uno spazio testuale con la scrollbar inserita
root2 = Tk()
root2.geometry('600x400')

root2.columnconfigure(0, weight=1)
root2.rowconfigure(0, weight=1)

scrolledtxt = scrolledtext.ScrolledText(root2, width=50, height=10)
scrolledtxt.pack(fill=BOTH, side=LEFT, expand=True)

root2.mainloop()