#Anahí Garcés
#8025-8030
import numpy as np
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
x=np.linspace(-3,3,100)
y=np.linspace(-3,3,100)

x,y=np.meshgrid(x,y)
z=np.sqrt(x**2+2*y**2)
ax.contourf(x,y,z)
plt.show()