#Anahí Garcés
#8025-8030
Lista=["ESPE","programa","unido","python"]
for cadena in Lista:
    print(cadena)
    for caracter in cadena:
        minuscula=caracter.lower()
        if minuscula in "aeoáéó":
            print(caracter.lower())