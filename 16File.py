#lavorare con file, leggere e scrivere
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry('600x400')

def apri_file():
    #quali tipi di file esistono
    filetypes = (
        ('file di testo', '*.txt'),
        ('tutti i file', '*.*')
    )
    #apri la finestra per aprire file. restituisce il percorso del file
    filename = filedialog.askopenfilename(title="apri un file", initialdir='/', filetypes=filetypes)
    
    #apri il file e fai la print del contenuto
    f = open(filename, 'r')
    data = f.read()
    print(data)
    f.close()

def salva_file():
    #salva file
    f = filedialog.asksaveasfile(mode='w', title="salva file", defaultextension='.txt')
    data = "ciao bello"
    f.write(data)
    f.close()

bottone = ttk.Button(root, text='apri file', command=apri_file)
bottone = ttk.Button(root, text='salva file', command=salva_file)
bottone.pack(expand=True)
root.mainloop()