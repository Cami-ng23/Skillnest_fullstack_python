#➡️ Pasar argumentos 
'''
Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__
y que de esta manera podamos asignarle a los atributos los valores correspondientes.
'''
class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

# Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 300)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 80000, 30000)
camilo = Usuario("Camilo", "Diaz", "deiberdiaz@liceovvh.cl", 100000, 4000)

#Imprimir datos
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#------------------Tarea------------------
#Crear una clase estudiante, y asignarle los siguientes atributos:
# (rut, nombre, apellido, especialidad, fecha nacimiento)
#Crear 3 instancias para la clase con distintos estudiantes
#imprimir el nombre y la edad de cada uno

class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.rut =rut
        self.fecha_nac = fecha_nac
camilo = Estudiante("25-551-900-k", "Camilo", "Diaz", "Programación", "20-10-2008")
luis = Estudiante("22-761-276-0", "Luis", "Maliqueo", "Programación", "10-04-2008")
diego = Estudiante("20-181-912-2", "diego", "Lopez", "Logistica", "12-02-2009")

print(camilo.nombre, camilo.apellido, camilo.especialidad)
print(luis.nombre, luis.apellido, luis.especialidad)
print(diego.nombre, diego.apellido, diego.especialidad)
