#Crear una clase llamada 'Animal' con los atributos nombre, edad y tipo, y mostrar la
#información del animal, incluyendo su nombre, edad y tipo, es necesario agregar que
#se deben crear dos objetos de la clase Animal para utilizar los métodos creados
class Animal:
    def __init__(self):
        self.nombre=input("ingrese el nombre de su mascota:")
        self.edad=input("Ingrese la edad de su mascota:")
        self.tipo=input("¿su mascota es felino, canino, ave, o algun otro?")
    def informacion(self):
        print("verifique si la información proporcionada es correcta:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Tipo: {self.tipo}")
mascota=Animal()
mascota.informacion()
