#Crear una clase llamada Vehículo
#atributos marca, modelo y color
#método que defina el precio del vehículo
#dos objetos de la clase Vehículo 
#método para establecer el precio de cada uno

class Vehiculo:
    def __init__(self):
        self.marca=("Toyota, Chevrolet, Nissan, Mercedez Benz")
        self.marca=(input("Colores disponibles: Rojo, Negro, Azul, Blanco, Gris"))
        self.modelo=("Toyota Corolla Cross 1.8 Xei Hybrid, Chevrolet Sonic 1.6 Lt 4 p, Nissan Sentra Sedan, Mercedez-Benz clase A 1.4 AMG line")
    def seleccion_de_auto(self):
     menu= '''
     1) Toyota Corolla Cross 1.8 Xei Hybrid
     2) Chevrolet Sonic 1.6 Lt 4 p
     3) Nissan Sentra Sedan
     4) Mercedez-Benz clase A 1.4 AMG line
     
     '''
     print(menu)
     op= int(input("Elige la opción que mas te haya gustado para conocer su precio:"))
     if op is 1:
         print("///////////////////////////////////////////////")
         print("/  Toyota Corolla Cross 1.8 Xei Hybrid:       /")
         print("/  Modelo 2024                                /")
         print("/  0km                                        /")
         print("/  Transminsión: Automática                   /")
         print("/  Combustible: Hibrido                       /")
         print("/  Puertas: 5                                 /")
         print("/  Valor: $131.000.000                        /")
         print("///////////////////////////////////////////////")
     elif op is 2: 
         print("///////////////////////////////////////////////") 
         print("/  Chevrolet Sonic 1.6 Lt:                    /")
         print("/  Modelo 2020                                /")
         print("/  1.600km                                    /")
         print("/  Motor: 1.6                                 /")
         print("/  Combustible: Gasolina                      /")
         print("/  Puertas: 4                                 /")
         print("/  Valor: $29.000.000                         /")
         print("///////////////////////////////////////////////")
     elif op is 3:
         print("///////////////////////////////////////////////")
         print("/  Nissan Sentra Sedan                         /")
         print("/  Modelo 1997                                /")
         print("/  12.000km                                   /")
         print("/  Motor: 1.6                                 /")
         print("/  Combustible: Gasolina                      /")
         print("/  Puertas: 4                                 /")
         print("/  Valor: $14.500.000                         /")
         print("///////////////////////////////////////////////")
     elif op is 4:
         print("///////////////////////////////////////////////")
         print("/  Mercedez-Benz clase A 1.4 AMG line         /")
         print("/  Modelo 2022                                /")
         print("/  12.000km                                   /")
         print("/  Motor: 1.4                                 /")
         print("/  Combustible: Gasolina                      /")
         print("/  Puertas: 5                                 /")
         print("/  Valor: $125.000.000                        /")
         print("///////////////////////////////////////////////")
       
auto=Vehiculo()
auto.seleccion_de_auto()
