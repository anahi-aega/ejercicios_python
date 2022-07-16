#Anahí Garcés
#8025-8030
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
#CREAR OBJETO
miMoto=Moto("Honda","FKL")
miMoto.caballito()
miMoto.estado()