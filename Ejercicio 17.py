# Ejercicio 17
# Cabecera: Deber
# David Viteri
n1=int(input("Ingrese el primer numero del tramo: "))
n2=int(input("Ingrese el ultimo numero del tramo: "))
lista=[]
for i in range(n1,n2+1):
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+j
    if c==i:
        lista.append(c) 
print("Los numeros perfectos del tramo son:",lista)
