#Anahí Garcés
#8025-8030
#Histograma
import numpy as np
import matplotlib.pyplot as plt
fig, ax=plt.subplots() #Crear la figura, graficar los ejes
#Media 5, D. ESTANDAR 1.5, DATOS 1000
x=np.random.normal(5,1.5,size=1000)
ax.hist(x,np.arange(0,11))
plt.show()