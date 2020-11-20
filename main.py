from functools import partial
from tkinter import *
from tkinter import ttk
from nodos import nodos


def imprimir(nodo):
    desplegable.set(nodo.estacion)


if __name__ == '__main__':

    raiz = Tk()
    raiz.geometry('1100x778')
    raiz.configure(bg='#FF5733')
    raiz.title("mapa")

    imagen = PhotoImage(file="mapa-metroatenas.png")
    fondo = Label(raiz, image=imagen).place(x=0, y=0)
    desplegable = ttk.Combobox(raiz, width=40,state="readonly")
    desplegable.place(x=750, y=100)
    botones=[]

    for i in nodos.values():

        boton=ttk.Button(raiz, text=i.estacion )
        boton.place(x=i.x, y=i.y)
        boton.configure(command=partial(imprimir,i))


    desplegable['values'] = list(nodos.keys())
    raiz.mainloop()
