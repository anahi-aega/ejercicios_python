import numpy as np
import time

V=1000000

#Listas

L1=range(V)
L2=range(V)

#
A1=np.arange(V)
A2=np.arange(V)

#Ejercicio sin Numpy
start=time.time()
result=[(x,y) for x,y in zip (L1,L2)]
print("Resultado sin numpy")
print((time.time()-start)*1000)

#Ejercicio con Numpy
start=time.time()
result=A1+A2
print("Resultado con Numpy")
print((time.time()-start)*1000)