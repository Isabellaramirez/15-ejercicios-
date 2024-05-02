#Crear una clase llamada Tablas con el atributo número, y un método llamado
#multiplicar que imprime la tabla de multiplicar deseada por el usuario, el método
#multiplicar recibe como parámetro el número hasta el cual se desea generar la tabla
#de multiplicar.
class Tablas:
    def __init__(self):
        self.numero=int(input("ingrese el numero de la tabla de multiplicar:"))
        self.limite=int(input("ingrese hasta que numero desea multiplicar"))
    def multiplicacion(self):
        for i in range(1,self.limite +1):
            resultado=i*self.numero
            print(f"{self.numero}x{i}={resultado}")
            
usuario=Tablas()
usuario.multiplicacion()
