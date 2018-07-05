from vpython import *
import numpy as np
b = box()

f1 = gcurve(color=color.cyan)	# curva de grafico

count = [0]

t=100

dt=1/t

n=0

l=arange(0, 10.0, 0.1)


##el bucle infinito que irá dibujando
while True:
    
    if len(count) <= 100:
        for x in count:	
            f1.plot(l[x],sin(l[x]))
        count.append(count[len(count)-1]+1)
    else:
        l=l+dt
        for x in l:
            f1.plot((x,sin(x)*x))

    rate(t) # esto pausará el gráfico
    f1.delete()
    n=n+dt
    
