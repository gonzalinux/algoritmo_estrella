from functools import partial
from tkinter import *
from tkinter import ttk
from nodos import Nodo
from Algoritmo2 import Algoritmo2


def imprimir(nodo):
    desplegable.set(nodo.estacion)


if __name__ == '__main__':

    raiz = Tk()
    raiz.geometry('1100x778')
    raiz.configure(bg='#FF5733')
    raiz.title("mapa")

    imagen = PhotoImage(file="mapa-metroatenas.png")
    #fondo = Label(raiz, image=imagen).place(x=0, y=0)
    desplegable = ttk.Combobox(raiz, width=40, state="readonly")
    desplegable.place(x=750, y=100)
    botones = []

    canvas = Canvas(width=710, height=778, bg="#FF5733")
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(710/2,778/2,image=imagen)


    canvas.create_line(10, 10, 80, 80)
    canvas.create_line(10, 80, 80, 10)





    nodos = Nodo().nodos
    origen=""
    destino=""
    algoritmo = Algoritmo2()
    recorrido = algoritmo.run(nodos.get("Halandri"), nodos.get("KAT"), list(nodos.values()))
    print("--------------------------")
    for i in recorrido:
        canvas.create_oval(i.x-7,i.y-7,i.x+7,i.y+7, outline="orange", fill="orange")
        canvas.create_line(i.x,i.y,i.antecesor.x,i.antecesor.y, width=4, fill="orange")


    """for i in nodos.values():
        boton = ttk.Button(raiz, text=i.estacion)
        boton.place(x=i.x, y=i.y)
        boton.configure(command=partial(imprimir, i))"""

    desplegable['values'] = list(nodos.keys())
    raiz.mainloop()
