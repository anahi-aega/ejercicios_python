#Anahí Garcés
#8025-8030
num_total=int(input("Cuántos números desea ingresar: "))
i=1
Resultado=0
total_pares=0
while i<=num_total:
    Numeros=int(input("Ingrese un numero: "))
    if Numeros%2==0:
        total_pares=total_pares+1
        print("Los números pares son: ",total_pares)
    elif Numeros%2!=0:
        Resultado=Numeros+Resultado
        print("La suma de los numeros impares es: ",Resultado)
    i=i+1
    print("------------------------------")
    print("El total de pares es: ",total_pares)
    print("El resultado de los impares es: ",Resultado)
print("Programa finalizado")