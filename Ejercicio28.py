#Anahí Garcés
#8025-8030
class Auto():
    def __init__(self):
        self.__largochasis=250
        self.__anchochasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()
        if (self.__enmarcha and chequeo):
            return "El auto está en marcha"
        elif (self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo y o se puede arrancar"
        else:
            return "El auto está parado"
    
    def estado (self):
        print("El auto tiene",self.__ruedas,"ruedas. Un ancho de",self.__anchochasis,"y un largo de:",self.__largochasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
#Instanciando clase, ejemplarizando clase, creando un objeto
miAuto=Auto()
miAuto.arrancar(True)
miAuto.estado()
#print(miAuto.__chequeo_interno())
print("Segundo objeto")
miAuto2=Auto()
print(miAuto2.arrancar(False))
miAuto2.ruedas=5
miAuto2.estado()