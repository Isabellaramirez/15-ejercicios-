class Cuenta:
    def __init__(self):
        self.titular = input("Ingrese el nombre del titular de la cuenta:")
        self.cantidadtenida = 400.000
        self.ingresar = int(input("Ingresa la cantidad a ingresar:"))
        self.retiros = int(input("Ingrese la cantidad a retirar:"))

    def actualizacion_data(self):
        ingresosfinales = self.retiros - self.cantidadtenida
        ingresostotales = self.cantidadtenida + self.ingresar
        print("En su cuenta hay:", ingresosfinales)
        print("Descontando el retiro en su cuenta hay:", ingresostotales)

usuario = Cuenta()
usuario.actualizacion_data()
