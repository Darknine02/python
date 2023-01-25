#tabular data e hierarchical data
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')

#diciamo tramite tupla i nomi delle colonne
colonne = ('nome', 'cognome', 'email')
#creiamo la tabella
tabella = ttk.Treeview(root, columns=colonne, show='headings')

#i nomi delle tabelle come devono essere mandati a schermo
tabella.heading('nome', text='Nome')
tabella.heading('cognome', text='Cognome')
tabella.heading('email', text='Email')

righe = []
#mettiamo in righe una tupla con nome e numero, ecc
for n in range(1,50):
    righe.append((f'nome {n}', f'cognome {n}', f'email {n}'))

#si inserisce ogni oggetto in righe nella tabella
for riga in righe:
    tabella.insert('', END, values=riga)
#mandiamo la tabella a schermo
tabella.grid(row=0, column=0, sticky='nsew')

#scrollbar
Scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tabella.yview)
Scrollbar.grid(row=0, column=1, sticky='ns')
tabella.configure(yscrollcommand=Scrollbar.set)

root.mainloop()