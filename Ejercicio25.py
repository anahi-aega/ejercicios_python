#Anahí Garcés
#8025-8030
print("Contador de sueltos autonamtico")
print()
print("Ingrese cuantas monedas tiene de cada tipo:")
cuartos=int(input("De 25 centavos: "))
dediez=int(input("De 10 centavos: "))
decinco=int(input("De 5 centavos: "))
centavos=int(input("De 1 centavo: "))
total=0.25*cuartos+0.10*dediez+0.05*decinco+0.01*centavos
print()
print("El valor del vuelto en dolares es:","$",total)