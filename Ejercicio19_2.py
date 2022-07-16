#Anahí Garcés
#8025-8030
print("a")
alimentos=["naranja","mermelada","harina","mandarina","ajo"]
precio= [0.80,1.10,0.90,1.30,0.45]
for i in range(len(alimentos)):
    if precio[i]<1:
        print(alimentos[i])