#creare, associare valore e variabile, generarla dinamicamente, mini esempio
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('600x400')

radioVar = StringVar()
#creare un radiobutton per m o f sulla variabile radioVar
r1 = Radiobutton(root, text="maschio", value="m", variable=radioVar)
r2 = Radiobutton(root, text="femmina", value="f", variable=radioVar)
r1.pack()
r2.pack()
button = Button(root, text='prova', command=lambda:print(radioVar.get())).pack()


#creiamo una variabile dove arriverà il risultato
taglia_selezionata = StringVar()
#una tupla contente più tuple con le taglie
taglie = (
    ('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra Large', 'XL'),
)

#scorriamo la tupla in taglia e creiamo un radiobutton con testo del valore 0 della tupla e il valore con il valore 1 della tupla
for taglia in taglie:
    r = ttk.Radiobutton(root, text=taglia[0], value=taglia[1], variable=taglia_selezionata)
    r.pack(padx=5, pady=5)
button = Button(root, text='Taglia', command=lambda:print(taglia_selezionata.get())).pack()

root.mainloop()