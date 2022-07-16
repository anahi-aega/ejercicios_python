#Anahí Garcés
#8025-8030
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
dias=["L","M","X","J","V","S","D"]
temperaturas={"Quito":[28.5,30.5,31,30,28,27.5,30.5],"Cuenca":[24.5,25.5,26.5,25,26.5,24.5,25]}
ax.plot(dias,temperaturas["Quito"],marker="^",linestyle="dashed", color="tab:purple")
ax.plot(dias,temperaturas["Cuenca"],marker=".", linestyle="dashdot",color="tab:green")
#Título
ax.set_title("Evoulución de temperatura diaria",loc="center",fontdict={"fontsize":14,"fontweight":"bold","color":"tab:blue"})
plt.show()