#creare un semplice menu, aggiungere separatore e sottomenu
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('600x400')

#barra menu principale
menubar = Menu(root)
#configurata su root
root.config(menu=menubar)

#creato un menu del sottomenu
file_menu = Menu(menubar, tearoff=0)
#abbiamo dato un comando sotto alla sezione file
file_menu.add_command(label='Exit', command=root.quit)
file_menu.add_command(label='New', command=root.quit)

#creiamo un sottomenu dentro il menu file
file_sub_menu = Menu(file_menu, tearoff=0)
file_sub_menu.add_command(label='ciao')
#creiamo il pulsante altro
file_menu.add_cascade(label='altro', menu=file_sub_menu)

file_menu.add_separator()
file_menu.add_command(label='Open', command=root.quit)

menubar.add_cascade(label='File', menu=file_menu)




root.mainloop()