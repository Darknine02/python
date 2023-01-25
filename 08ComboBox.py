#creare, inserire valori, esempio con mesi, readonly state, associare evento
from tkinter import *
from tkinter import ttk
from calendar import month_name

root = Tk()
root.geometry('600x400')

#menu a tendina
mese_selezionato = StringVar()
#creiamo una combobox che mette sulla variabile
combobox = ttk.Combobox(root, textvariable=mese_selezionato)
#inseriamo i dati in automatico dentro il menu a tendina usando il modulo calendar
combobox['values'] = [month_name[m] for m in range(1,13)]
#mettiamo che non si può scrivere
combobox['state'] = 'readonly'
combobox.pack(fill=X, padx=5, pady=5)

def seleziona_mese(event):
    print(mese_selezionato.get())

#creiamo un evento combobox che chiama la funzione
combobox.bind('<<ComboboxSelected>>', seleziona_mese)

root.mainloop()