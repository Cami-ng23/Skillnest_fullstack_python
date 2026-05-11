'''
Define la clase SuscripcionStreaming, que debe incluir:

Atributos:
usuario (nombre del usuario asociado a la suscripción)
tipo_suscripcion (Gratis, Estándar, Premium)
costo_mensual (según el tipo de suscripción)
saldo_pendiente (monto acumulado que debe pagar el usuario)
Métodos:
realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.
Realizar las siguientes pruebas con instancias:

Crea 3 usuarios con diferentes tipos de suscripción.
Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.
'''

class PlataformaVideo:

    planes = {"Basico": 0, "Plus": 6.99, "Ultra": 12.99}

    def __init__(self, nombre, plan="Basico"):
        self.nombre = nombre
        self.plan = plan
        self.total_pagar = 0

    def agregar_pago(self, monto):
        self.total_pagar += monto
        print(f"{self.nombre} pagó ${monto}. Total acumulado: ${self.total_pagar}")

    def cambiar_plan(self, nuevo_plan):
        if nuevo_plan in self.planes:
            self.plan = nuevo_plan
            print(f"{self.nombre} ahora tiene el plan {nuevo_plan}")
        else:
            print("Plan no disponible")

    def ver_contenido(self):
        if self.plan == "Basico":
            print(f"{self.nombre} solo puede ver contenido normal")
        else:
            print(f"{self.nombre} puede ver contenido premium")

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre}")
        print(f"Plan actual: {self.plan}")
        print(f"Total pagado: ${self.total_pagar}")


# ---------------- USUARIOS ----------------

cliente1 = PlataformaVideo("Matias", "Basico")
cliente2 = PlataformaVideo("Fernanda", "Plus")
cliente3 = PlataformaVideo("Ignacio", "Ultra")


print("\n--- Cliente 1 ---")
cliente1.ver_contenido()
cliente1.agregar_pago(6.99)
cliente1.cambiar_plan("Plus")

print("\n--- Cliente 2 ---")
cliente2.ver_contenido()
cliente2.agregar_pago(12.99)
cliente2.cambiar_plan("Ultra")

print("\n--- Cliente 3 ---")
cliente3.ver_contenido()
cliente3.agregar_pago(3.50)

print("\n--- DATOS FINALES ---")
cliente1.mostrar_datos()
cliente2.mostrar_datos()
cliente3.mostrar_datos()