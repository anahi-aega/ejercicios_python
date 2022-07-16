#Anahí Garcés
#8025-8030
class Auto ():
    #propiedades
    largochasis=250
    anchochasis=120
    ruedas=4
    enmarcha=False #estabilidad inicial detenido
#creando método arrancar
    def arrancar (self):
        self.enmarcha=True #Arranco el objeto
#crear método estado
    def estado (self):
        if (self.enmarcha):
            print("El auto está en marcha")
        else:
            return "El auto está detenido" 
#creando objeto
miAuto=Auto()
print("El largo del auto es:",miAuto.largochasis)
print("El auto tiene:",miAuto.ruedas,"ruedas")
print("El ancho del auto es:",miAuto.anchochasis)
miAuto.arrancar()
print(miAuto.estado())

miAuto2=Auto()
print("El ancho del chasis es:",miAuto2.anchochasis)
print("El auto tiene",miAuto2.ruedas,"ruedas")
miAuto2.arrancar()
print(miAuto2.estado())