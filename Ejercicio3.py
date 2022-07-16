# Tarea #1 - Ejercicio 3
# Juan Suntaxi
# NRC 8025-8030

#Función que traduce los dígitos a su respectivo hexadecimal
def CambiarDigitos(digitos):
    decimales = [10,11,12,13,14,15]
    hexadecimal = ["A","B","C","D","E","F"]
    for i in range(7):
        if digitos == decimales [i - 1]:
            digitos = hexadecimal [i - 1]
    return digitos

decimal = int (input("\nIngrese el decimal: " )) 
hexadecimal = ""  
while decimal != 0:
    rem = CambiarDigitos ( decimal%16 )
    hexadecimal = str(rem) +  hexadecimal
    decimal = int (decimal/16)
print("\nEl número en hexadecimal es: " + hexadecimal,"\n") 

