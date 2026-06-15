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

class SuscripcionStreaming:

    planes = {"Gratis": 0, "Estándar": 6.99, "Premium": 12.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.planes[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto

        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"{self.usuario} pagó ${monto}. Saldo pendiente: ${self.saldo_pendiente}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.planes:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.planes[nuevo_tipo]
            print(f"{self.usuario} ahora tiene la suscripción {nuevo_tipo}")
        else:
            print("Tipo de suscripción no disponible")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print(f"{self.usuario} no tiene acceso a contenido exclusivo")
        else:
            print(f"{self.usuario} puede ver contenido exclusivo")

    def mostrar_info_suscripcion(self):
        print(f"Usuario: {self.usuario}")
        print(f"Tipo de suscripción: {self.tipo_suscripcion}")
        print(f"Costo mensual: ${self.costo_mensual}")
        print(f"Saldo pendiente: ${self.saldo_pendiente}")


# ---------------- USUARIOS ----------------

usuario1 = SuscripcionStreaming("Matias", "Gratis")
usuario2 = SuscripcionStreaming("Fernanda", "Estándar")
usuario3 = SuscripcionStreaming("Ignacio", "Premium")


print("\n--- Usuario 1 ---")
usuario1.ver_contenido_exclusivo()
usuario1.cambiar_suscripcion("Estándar")
usuario1.realizar_pago(6.99)


print("\n--- Usuario 2 ---")
usuario2.ver_contenido_exclusivo()
usuario2.cambiar_suscripcion("Premium")
usuario2.realizar_pago(5)
usuario2.realizar_pago(7.99)


print("\n--- Usuario 3 ---")
usuario3.realizar_pago(3.50)
usuario3.ver_contenido_exclusivo()


print("\n--- INFORMACIÓN FINAL ---")
usuario1.mostrar_info_suscripcion()
usuario2.mostrar_info_suscripcion()
usuario3.mostrar_info_suscripcion()