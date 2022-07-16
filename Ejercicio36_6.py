#Anahí Garcés
class persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar_residencia

    def descripcion(self):
        print("Nombre del empleado:",self.nombre,"\nEdad del empleado:",self.edad,"\nLugar de residencia:",self.lugar)

class empleado(persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,lugar_empleado):
        super().__init__(nombre_empleado,edad_empleado,lugar_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario:",self.salario,"\nAntigüedad:",self.antiguedad)

#CREAR UN OBJETO
Luis=empleado("1500","15","Luis","55","Cuenca")
Luis.descripcion()

print("\nAntonio\n")
Antonio=persona("Antonio","38","Cali")
Antonio.descripcion

print(isinstance (Luis,empleado)) #el objeto Luis pertenece a la clase persona
print(isinstance(Luis,persona)) #el objeto Luis pertenece a la superclase persona
print(isinstance(Antonio,persona))
print(isinstance(Antonio,empleado))