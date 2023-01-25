#importare db, installare mydql connector, inserire dati di prova
#select, insert, update, delete
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.geometry('600x400')

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='biblioteca'
)

cursore = db.cursor()
cursore.execute("select * from libri")
risultato = cursore.fetchall()

colonne = ('id', 'titolo', 'autore')
tabella = ttk.Treeview(root, columns=colonne, show='headings')
tabella.heading('id', text='ID')
tabella.heading('titolo', text='Titolo')
tabella.heading('autore', text='Autore')

for riga in risultato:
    tabella.insert('', END, values=riga)

tabella.grid(row=0, column=0, sticky="nsew")

def inserisci():
    inserisci_sql = "INSERT INTO libri(titolo, autore) values (%s, %s)"
    inserisci_valori = ("il mago di oz", 'bello figo')

    cursore.execute(inserisci_sql, inserisci_valori)
    db.commit()
def modifica():
    modifica_sql = "update libri set titolo = 'il mago di oz' where id = 3"

    cursore.execute(modifica_sql)
    db.commit()
def elimina():
    elimina_sql = "DELETE FROM libri where id = 2"
    cursore.execute(elimina_sql)
    db.commit()

inserisci_btn = Button(root, text='inserisci', command=inserisci)
modifica_btn = Button(root, text='modifica', command=modifica)
elimina_btn = Button(root, text='elimina', command=elimina)

inserisci_btn.grid(row=1, column=0)
modifica_btn.grid(row=2, column=0)
elimina_btn.grid(row=3, column=0)

root.mainloop()