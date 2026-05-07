# Atributos, métodos de clase, métodos estáticos

#Definición de la clase
class Estudiante: 
    #Atributo de clase 
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes 
    estudiantes = []
    
    #Metodo constructor 
    def __init__(self, nombre, nota):
        #Atributos de instrancias
        self.nombre = nombre
        self.nota = nota
        
        
#Agregar elementos a lista Estudiante(objeto)
        Estudiante.estudiantes.append(self)
    
    #Metodo de instancia
    def mostrar_info(self):
        print(f"Nombre : {self.nombre}")
        print(f"Nota : {self.nota}")

    #Metodo de clase 
    #Usa "cls" porque trabaja con la información de la clase 
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre
        
    @classmethod # Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    #Método estático
    # Este no usar cls ni self, solo parametros
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False 
    
#Creación de objetos(instancias)
e1 = Estudiante("camilo", 7.0)
e2 = Estudiante("donovan", 6.4)
e3 = Estudiante("matias", 3.2)

#Uso de métodos de instancia
print("==MÉTODO DE INSTANCIA==")
e1.mostrar_info()
print()
e2.mostrar_info()
print()
e3.mostrar_info()
print()

#usar Atributo de clase
print("===ATRIBUTO DE CLASE===")
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

#Uso de metodo de clase
print("===METODO DE CLASE===")
Estudiante.cambiar_colegio("Purkuyen")
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)

#Contar Estudiante 
print("===CONTAR ESTUDIANTES ===")
print(f"Total estudiantes : {Estudiante.cantidad_estudiantes()}")

#MÉTODO estático
print("===MÉTODO ESTÁTICO===")
print(f"{e1.nombre} aprueba?")
print(Estudiante.aprobar(e1.nota))
print()

print(f"{e2.nombre} aprueba?")
print(Estudiante.aprobar(e2.nota))
print()

print(f"{e3.nombre} aprueba?")
print(Estudiante.aprobar(e3.nota))
print()



## Función repaso.
# Crear Función que valide usuario y contraseña

def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}")
        return True
    else:
        print("Acceso denegado")
        return False
    
def enviarDatos():
    username = input( "Ingrese su nombre usuario : ")
    password = input("Ingrese su contraseña : ")
    validator = validador(username, password)

enviarDatos()