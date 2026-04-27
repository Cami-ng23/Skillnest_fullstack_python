class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 3000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
    
    def aunmentar_credido(self, aunmento):
        self.limite_credito += aunmento
        
    def cambiar_correo(self, email):
        self.email = email  
#Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(0)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
miyagi.hacer_compra(3000)
print(f"Segunda compra : ${miyagi.saldo_pagar}")
#Imprimir cuanto credido le queda a miyagi
print(f"Le quedan {miyagi.limite_credito - miyagi.saldo_pagar}")
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45

miyagi.aunmentar_credido(10000)
print(f"El nuevo limite de credido es : {miyagi.limite_credito}")

#Tarea
'''
Crear un nuevo método que permita aunmentar el limite de crédido 
Imprimir el nuevo limite 

2.-Crear un método que permita cambiar el correo de la instancia 
Mostrar el nuevo correo
'''
miyagi.cambiar_correo("miyagiabc@gmail.com")
print(f"el nuevo correo es {miyagi.email}")