#creare, callback, prendere valore checkbox, cambiare valore predefiniti
from tkinter import *
from tkinter import ttk

#con la funzione si può creare nuove parti della finestra attraverso la checkbox se è attiva o no
def premo_check():
    label = Label(text=nome.get())
    label.pack()

root = Tk()
root.geometry('600x400')

nome = StringVar()
#CheckBox con testo ciao, fa il print della variabile nome StringVar, se la checkbox è on la variabile ci sarà luca altrimenti marco
check = Checkbutton(text="Ciao", font=('Helvetica', 20), command=premo_check, variable=nome, onvalue='luca', offvalue='marco')
check.pack()

root.mainloop()