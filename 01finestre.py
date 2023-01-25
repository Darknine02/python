#Finestre, title, geometry e icona
#resizable, dimensioni minime e massime, trasparenza
#stack con topmost, lift e lower

from tkinter import *
#from tkinter import tkk

#Creare una nuova finestra
root = Tk()
#aggiungere un titolo alla finestra
root.title("La nostra finestra")

#geometria
root.geometry('600x400+50+50')

#icona
root.iconbitmap('Tkinter/icona.ico')

#poter trascinare la finestra
root.resizable(True, False)

root.minsize(400, 100)
root.maxsize(1000, 1000)

#trasparenza della finestra
root.attributes("-alpha", 0.5)

#finestra sempre sopra
root.attributes('-topmost', 1)
#portare la finestra sopra quando si crea
root.lift()
#portare la finestra dietro quando si crea
root.lower()


#Per mantenere il programma costantemente aperto
root.mainloop()