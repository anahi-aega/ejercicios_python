#Anahí Garcés
#8025-8030
import matplotlib.pyplot as plt
fig, ax=plt.subplots(2,2,sharey=True)
dias=["L","M","X","J","V","S","D"]
temperaturas={"Quito":[28.5,30.5,31,30,28,27.5,30.5],"Cuenca":[24.5,25.5,26.5,25,26.5,24.5,25]}
ax[0,0].plot(dias,temperaturas["Quito"])
ax[0,1].plot(dias,temperaturas["Cuenca"],color="tab:orange")
ax[1,0].plot(dias,temperaturas["Quito"],color="tab:purple")
ax[1,1].plot(dias,temperaturas["Cuenca"])

plt.show()