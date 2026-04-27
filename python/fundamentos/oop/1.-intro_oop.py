# Esta es la sintaxis para crear una clase llamada Usuario:
class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0
pass #Pronto pondremos métodos y atributos

# Y para crear una nueva instancia de nuestra clase se vería como:
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
camilo = Usuario("Camilo", "Diaz", "deiberdiaz@liceovvh.cl")

print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(camilo.nombre)
