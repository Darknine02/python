#messaggio di info, errore e warning. si/no, ok/cancella, riprova/cancella
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('600x400')

def show_message():
    #messaggi di info, error e warning
    messagebox.showinfo(title='info', message='Questo è un messaggio di informazione')
    messagebox.showerror(title='info', message='Questo è un messaggio di informazione')
    messagebox.showwarning(title='info', message='Questo è un messaggio di informazione')
    #messaggi con si o no, riprova o altro
    risposta = messagebox.askyesno(title='Prova', message="vuoi uscire?")
    #se la risposta è stata si chiudi il programma
    if risposta:
        root.destroy()

button = ttk.Button(root, text='mostra messaggio', command=show_message).pack(fill=BOTH)

root.mainloop()