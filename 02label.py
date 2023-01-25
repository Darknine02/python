#creare label e mostrarla, background, curosre
#font, foreground, allineamento, padding, immagine

from tkinter import *

root = Tk()
root.geometry('600x400')

#creare etichette, color background, padding, colore scritta e font, cambio cursor, allineamento, aggiungere una immagine in posizione top alla scritta
photo = PhotoImage(file='Tkinter/instagram.png')
label = Label(text='Ciao \n Sono un computer', background='red', padx=50, pady=50, foreground='white', 
              font=('Helvetica', 24), cursor='clock', justify='center', image=photo, compound='top')
label.pack()

root.mainloop()