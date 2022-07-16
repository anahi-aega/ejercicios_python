#Anahí Garcés
#PROPIEDADES COMUNES
class vehiculos():
    def __init__ (self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelerar=False
        self.frenar=False

#COMPORTAMIENTOS COMUNES
    def arrancar (self):
        self.enmarcha=True
    def frenar (self):
        self.frenar=True
    def acelerar (self):
        self.acelerar=True
    def estado (self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.enmarcha,"\nAcelerado:",self.acelerar,"\nFrenando:",self.frenar)

#CREAR LA CLASE QUE HEREDA
class Moto(vehiculos):
    #COMPORTAMIENTO PARTICULAR
    hcaballito=""
    def caballito(self):
        self.hcaballito="Estoy realizando la maniobra caballito"
    def estado (self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.enmarcha,"\nAcelerado:",self.acelerar,"\nFrenando:",self.frenar,"\nManiobra:",self.hcaballito)

class Furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class vehiculos_electricos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.acelerar=False
        self.frenar=False
        self.autonomia=100
        
    def carga_energia(self):
        self.cargando=True

class bicicleta_electrica(vehiculos_electricos,vehiculos):
    pass

#CREAR OBJETO
print("\nMoto\n")
miMoto=Moto("Honda","FKL")
miMoto.caballito()
miMoto.estado()

print("\nFurgoneta\n")
miFurgoneta=Furgoneta("Marca F","Modelo F")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(False))

print("\nBicicleta\n")
miBicicleta=bicicleta_electrica("Marca Elect","Modelo Elect")
miBicicleta.arrancar()
miBicicleta.estado()