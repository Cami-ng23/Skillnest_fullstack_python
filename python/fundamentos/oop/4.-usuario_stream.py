'''
Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
🧪 Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.
'''

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(contenido)
        print(f"{contenido} agregado a la lista de {self.nombre}")
    pass


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print("El usuario {self.nombre} esta viendo {titulo}")
        else: 
            print(f"Titulo no encontrado {titulo}")
    pass


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        self.suscripcion = nueva_suscripcion
        print(f"{self.nombre} cambió su suscripción a {nueva_suscripcion}")
        pass


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print("\n--- INFO USUARIO ---")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        print("Lista de reproducción:")
        for item in self.lista_reproduccion:
            print(f"- {item}")

camilo = UsuarioStreaming("Carlos", "carlos@email.com")
camilo.agregar_a_lista("Breaking Bad")
camilo.agregar_a_lista("Stranger Things")
camilo.ver_contenido("Breaking Bad")
camilo.ver_contenido("Stranger Things")
while True:
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1.- Ejercicio 1")
    print("2.- Ejercicio 2")
    print("3.- Ejercicio 3")
    print("4.- Ejercicio 4")
    print("0.- Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_a_lista()
    elif opcion == "2":
        ver_contenido()
    elif opcion == "3":
        cambiar_suscripcion()
    elif opcion == "4":
        mostrar_info_usuario()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")
    
    

