#threading con più processi
from tkinter import *
from tkinter import ttk
import time
import threading

root = Tk()
root.geometry('600x400')

def dormi():
    time.sleep(5)
    print('stavo dormendo')

def mangia():
    print('sto mangiando')

button = Button(root, text='dormi', command=lambda: threading.Thread(target=dormi).start()).pack(expand=True, fill=X)
button = Button(root, text='mangia', command=mangia).pack(expand=True, fill=X)
root.mainloop()