#creare, personalizzare, aggiungere comando callback e lambda (funzione in linea)
#stato disabilitato, bottone immagine, immagine e testo
from tkinter import *
from tkinter import ttk
def saluta():
    print('Ho cliccato il bottone')

root = Tk()
root.geometry('600x400')

photo = PhotoImage(file='Tkinter/instagram.png')

#creazione pulsante con comando
button = Button(text="ciao", background='red', foreground='blue', width=20, borderwidth=3, command=saluta)
#si può prendere il bottone da ttk per avere uno stato disabilitato, può contenere una immagine e testo
button2 = ttk.Button(text="esci", command=lambda: root.quit(), image=photo, compound="left")
button.pack()
#state disabilitato
button2.state(['disabled'])
button2.pack()

root.mainloop()