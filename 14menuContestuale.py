#context menu
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')

#crea un frame contenitore
frame = Frame(root, background='red')
frame.pack(expand=True, fill=BOTH)

#creiamo il menu
ctx_menu = Menu(root, tearoff=0)
ctx_menu.add_command(label="Taglia")
ctx_menu.add_command(label="Copia")
ctx_menu.add_command(label="Incolla")
ctx_menu.add_separator()
ctx_menu.add_command(label="Prova")

#funzione che prova a creare il menu nella x e y dove si è cliccato
def ctx_menu_popup(event):
    try:
        ctx_menu.tk_popup(event.x_root, event.y_root)
    finally:
        ctx_menu.grab_release()

#assegna il tasto destro
frame.bind("<Button-3>", ctx_menu_popup)
root.mainloop()