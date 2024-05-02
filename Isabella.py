#ejercicio de Isabella
#Crear una clase llamada 'Empresa' que gestione la información de los empleados,
#incluyendo el nombre del empleado, los días trabajados, el salario de la persona y la
#nómina total de la empresa. Cada día de trabajo equivale a $40,000. Se deben crear
#dos objetos de la clase Empresa para utilizar los métodos creados. Mostrar el nombre
#del empleado junto a los días trabajados y al salario de esa persona. Finalmente,
#mostrar la nómina total de la empresa."

class Empresa:
    def __init__ (self):
        self.nombre_empleado = (input("ingrese su nombre:"))
        self.dias_trabajados = int(input("ingrese la cantidad de dias trabajados"))
        self.salario = 40000 * self.dias_trabajados
        self.nomina_total = self.salario
        
    def datos_empleado(self):
        print(f"Nombre del empleado:{self.nombre_empleado}")
        print(f"Sus dias trabajados fueron:{self.dias_trabajados}")
        print(f"Su salario de este mes es:{self.salario}")
        
print("Bienvenido aqui podra ver los resultados del mes")
print("si va a continuar con el proceso por favor escriba: 'si', de lo contrario escriba alguna otra palabra")
total_salario=0
while input("¿Continuará?") == "si":
    empleados=Empresa()
    empleados.datos_empleado()    
    total_salario += empleados.salario
    print("La nomina de este mes de la empresa es:", total_salario)
