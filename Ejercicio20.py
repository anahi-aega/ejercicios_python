#Anahí Garcés
#8025-8030
sensores=["temperatura","distancia","temperatura","luz","humedad"]
precio=[5,10,3,5,10]
clientes=["Alex","Diana","Santiago","Sergio","Daniela"]
#quien y cantidad o precio
for i in range (len(sensores)):
    sensor=sensores[i]
    if sensor=="temperatura":
        print(clientes[i])
        print (precio[i])
