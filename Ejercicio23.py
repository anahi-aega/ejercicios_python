#Anahí Garcés
#8025-8030
print("Bienvenido a tu calculadora")
print("1) Suma")
print("2) Resta")
print("3) Salir")
opcion = input("Ingrese una opcion: ")
while opcion!=3:
    if (opcion=="1"):
        n1= int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese un numero: "))
        total = n1+n2
        print("La suma de los numeros es: ", total)
        break
    elif (opcion=="2"):
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese un numero: "))
        total = n1 - n2
        print("La suma de los numeros es: ", total)
        break
    if (opcion=="3"):
        print("Fin de la calculadora")
        break
