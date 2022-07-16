# Tarea #1 - Ejercicio 6
# Juan Suntaxi
# NRC 8025-8030

n = eval(input("\nIngrese un número (digite 999 para finalizar el ingreso): "))

if n%2 == 0:
    pares = [n]

multiplos5 = []
impares = []
suma = 0

while n != 999:
    n = eval(input("\nIngrese un número (digite 999 para finalizar el ingreso): "))

    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        suma = suma + n
        promedio = suma/len(impares)

    if n%5 == 0:
        multiplos5.append(n)
        

print("\nLa cantidad de números pares ingresados es",len(pares))
print("La cantidad de multiplos de 5 ingresados es",len(multiplos5))
print("El promedio de los números impares es: ",promedio,"\n")

