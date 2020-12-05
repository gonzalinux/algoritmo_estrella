import os
import sys
import tkinter.font as tkFont
from functools import partial
from tkinter import *

from Algoritmo import Algoritmo
from nodos import Nodo


# funcion auxiliar para el empaquetado del programa,
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


#  Clase para ejecutar cambios en la interfaz grafica
class Cambiar:
    def __init__(self):
        self.origen = None
        self.destino = None
        self.selecionado1 = False
        self.selecionado2 = False
        self.algoritmo = Algoritmo()
        self.nodos = Nodo().nodos.copy()

    # la funcion reset deja el estado inicial
    def reset(self):
        self.origen = None
        self.destino = None
        self.selecionado1 = False
        self.selecionado2 = False
        nodoselecionado1.configure(state="normal")
        nodoselecionado1.delete("1.0", END)
        nodoselecionado1.insert(INSERT, "No ha seleccionado nada")
        nodoselecionado1.configure(state="disabled")
        nodoselecionado2.configure(state="normal")
        nodoselecionado2.delete("1.0", END)
        nodoselecionado2.insert(INSERT, "No ha seleccionado nada")
        nodoselecionado2.configure(state="disabled")
        djrecorrida.configure(state="normal")
        djrecorrida.delete("1.0", END)
        djrecorrida.insert(INSERT, "No hay seleccion")
        ntrans.configure(state="disabled")
        ntrans.configure(state="normal")
        ntrans.delete("1.0", END)
        ntrans.insert(INSERT, "No hay seleccion")
        ntrans.configure(state="disabled")
        nest.configure(state="disabled")
        nest.configure(state="normal")
        nest.delete("1.0", END)
        nest.insert(INSERT, "No hay seleccion")
        nest.configure(state="disabled")
        tiempo.configure(state="disabled")
        tiempo.configure(state="normal")
        tiempo.delete("1.0", END)
        tiempo.insert(INSERT, "No hay seleccion")
        tiempo.configure(state="disabled")

        canvas.delete("all")
        canvas.create_image(710 / 2, 778 / 2, image=imagen)
        self.algoritmo = Algoritmo()
        self.nodos = Nodo().nodos.copy()
        for nodo in list(nodos.values()):
            nodo.antecesor = None

    # Funcion que recibe el nodo pulsado en el mapa
    def selecion_nodo(self, nodo):

        if not self.selecionado1:
            nodoselecionado1.configure(state="normal")
            nodoselecionado1.delete("1.0", END)
            nodoselecionado1.insert(INSERT, nodo.estacion)
            nodoselecionado1.configure(state="disabled")
            self.origen = nodo
            self.selecionado1 = True
        else:
            nodoselecionado2.configure(state="normal")
            nodoselecionado2.delete("1.0", END)
            nodoselecionado2.insert(INSERT, nodo.estacion)
            nodoselecionado2.configure(state="disabled")
            self.destino = nodo
            canvas.delete("all")
            canvas.create_image(710 / 2, 778 / 2, image=imagen)
            self.algoritmo = Algoritmo()
            self.nodos = Nodo().nodos.copy()
            for nodo in list(nodos.values()):
                nodo.antecesor = None
            self.mostrar_camino()

    # funcion para mostrar el recorrido una vez selecionados nodos origen y destino
    def mostrar_camino(self):
        for boton in botones:
            boton.pack_forget()

        recorrido = self.algoritmo.run(self.origen, self.destino, list(self.nodos.values()))

        for sitio in recorrido:
            canvas.create_oval(sitio.x - 7, sitio.y - 7, sitio.x + 7, sitio.y + 7, outline="#f491ff", fill="#f4917f")
            canvas.create_line(sitio.x, sitio.y, sitio.antecesor.x, sitio.antecesor.y, width=6, fill="#f491f7")
        djrecorrida.configure(state="normal")
        djrecorrida.delete("1.0", END)
        djrecorrida.insert(INSERT, str(self.algoritmo.dist / 1000) + " KM")
        djrecorrida.configure(state="disabled")
        ntrans.configure(state="normal")
        ntrans.delete("1.0", END)
        ntrans.insert(INSERT, str(self.algoritmo.ntrans))
        ntrans.configure(state="disabled")
        nest.configure(state="normal")
        nest.delete("1.0", END)
        nest.insert(INSERT, str(len(recorrido)))
        nest.configure(state="disabled")
        tiempo.configure(state="normal")
        tiempo.delete("1.0", END)
        tiempo.insert(INSERT, str(
            int(len(recorrido) * 2 + (self.algoritmo.dist / 1000) / (80 * 60) + self.algoritmo.ntrans * 5))
                      + "minutos")
        tiempo.configure(state="disabled")


# proceso proncipal del programa
if __name__ == '__main__':
    cambiar = Cambiar()
    selecionado1 = False
    selecionado2 = False
    destino = None
    origen = None
    # Se usa tkinter para el desarrollo grafico
    raiz = Tk()
    fontStyle = tkFont.Font(family="Yu Gothic Light", size=15)
    fontStyle2 = tkFont.Font(family="MS UI Gothic", size=20)
    fontStyle3 = tkFont.Font(family="MS UI Gothic", size=30)
    raiz.geometry('1100x778')
    raiz.configure(bg='#d7e1ed')
    raiz.title("mapa")
    # se carga la imagen del mapa y los botones
    imagen = PhotoImage(file=resolver_ruta("mapa-metroatenas.png"))
    imagencir = PhotoImage(file=resolver_ruta("imgbot.png"))



    canvas = Canvas(width=710, height=778, bg="#d7e1ed")
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(710 / 2, 778 / 2, image=imagen)

    nodos = cambiar.nodos
    algoritmo = Algoritmo()

    botones = []
    j = 0
    #se crean todos los botones correspondientes a cada nodo
    for i in nodos.values():
        botones.append(Button(raiz, image=imagencir, bg="#3e30a6", width=10, height=10))
        botones[j].pack()
        botones[j].place(x=i.x - 5, y=i.y - 5)
        #cuando se presione el boton se ejecuta la selecion de nodo
        botones[j].configure(command=partial(cambiar.selecion_nodo, i))

        j += 1
    #resto de apartados graficos.
    info0 = Label(raiz, text="Calculador de rutas \ndel metro de Atenas", bg="#d7e1ed", font=fontStyle3)
    info0.place(x=740, y=40)
    info1 = Label(raiz, text="Punto de Origen:", bg="#d7e1ed", font=fontStyle)
    info1.place(x=750, y=200)

    nodoselecionado1 = Text(raiz, bg="#d7e1ed", border=0, font=fontStyle2, )

    nodoselecionado1.pack()
    nodoselecionado1.place(x=750, y=250)
    nodoselecionado1.insert(INSERT, "No ha seleccionado nada", )
    nodoselecionado1.configure(state="disabled")

    info2 = Label(raiz, text="Punto de Destino:", bg="#d7e1ed", font=fontStyle)
    info2.place(x=750, y=300)

    nodoselecionado2 = Text(raiz, bg="#d7e1ed", border=0, font=fontStyle2)

    nodoselecionado2.pack()
    nodoselecionado2.place(x=750, y=350)
    nodoselecionado2.insert(INSERT, "No ha seleccionado nada")
    nodoselecionado2.configure(state="disabled")

    reset = Button(raiz, bg="#d7e1ed", text="RESET", font=fontStyle)
    reset.place(x=750, y=400)
    reset.configure(command=partial(cambiar.reset))

    info3 = Label(raiz, text="Distancia Recorrida: ", bg="#d7e1ed", font=fontStyle)
    info3.place(x=750, y=450)

    djrecorrida = Text(raiz, bg="#d7e1ed", font=fontStyle)
    djrecorrida.pack()
    djrecorrida.configure(width=30, height=1)
    djrecorrida.place(x=750, y=480)
    djrecorrida.insert(INSERT, "No hay seleccion")
    djrecorrida.configure(state="disabled")

    info4 = Label(raiz, text="Nª transbordos: ", bg="#d7e1ed", font=fontStyle)
    info4.place(x=750, y=530)

    ntrans = Text(raiz, bg="#d7e1ed", font=fontStyle)
    ntrans.pack()
    ntrans.configure(width=30, height=1)
    ntrans.place(x=750, y=560)
    ntrans.insert(INSERT, "No hay seleccion")
    ntrans.configure(state="disabled")

    info5 = Label(raiz, text="Nª estaciones: ", bg="#d7e1ed", font=fontStyle)
    info5.place(x=750, y=610)

    nest = Text(raiz, bg="#d7e1ed", font=fontStyle)
    nest.pack()
    nest.configure(width=30, height=1)
    nest.place(x=750, y=640)
    nest.insert(INSERT, "No hay seleccion")
    nest.configure(state="disabled")

    info6 = Label(raiz, text="Tiempo estimado: ", bg="#d7e1ed", font=fontStyle)
    info6.place(x=750, y=690)

    tiempo = Text(raiz, bg="#d7e1ed", font=fontStyle)
    tiempo.pack()
    tiempo.configure(width=30, height=1)
    tiempo.place(x=750, y=720)
    tiempo.insert(INSERT, "No hay seleccion")
    tiempo.configure(state="disabled")

    raiz.mainloop()
