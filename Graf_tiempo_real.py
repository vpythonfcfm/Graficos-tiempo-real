import numpy as np
import matplotlib.pyplot as plt
import tkinter

pause = True
stop = False

def Pausar():
   global pause
   pause = not pause
def Parar():
   global stop
   stop = not stop

## Botones para pausar y parar el loop del gráfico

root = tkinter.Tk()
boton1 = tkinter.Button(root, text="Pausar", command=Pausar).place(x=23,y=10)
boton2 = tkinter.Button(root, text="Parar", command=Parar).place(x=23,y=50)

plt.ion() # hace el gráfico interactivo

dt=1/10

n=0

y = [] # lista vacia que se ira llenando con datos
x = []

## el bucle infinito que irá dibujando
while True:
    ## añadimos elementos a los ejes
    x.append(n)
    y.append(np.sin(n)*n)

    if len(y) <= 100:
        plt.plot(x,y)
    else:
        ## proboca que se mueva el gráfico
        plt.plot(x[-100:],y[-100:])

    plt.pause(0.005) # esto pausará el gráfico
    n=n+dt
    while pause == False:
       plt.pause(0.1)
    plt.cla() # esto limpia la información del axis (el área blanca donde se pintan las cosas)
    if stop == True:
       break
plt.close()
