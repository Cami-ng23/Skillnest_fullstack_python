from usuario import Usuario

while True:

    print("\n-------- VERIFICIÓN DE USUARIOS-----")
    print("1. Iniciar sesión")
    print("2. Salir")

    opcion = input("Opción: ")

    if opcion == "1":

        usuario = input("Ingresar Usuario: ")
        password = input("Ingresar Password: ")

        u = Usuario(usuario=usuario, password=password)
        datos = u.login()

        if datos:

            print("\nHola, Bienvenido:", datos[1])

            if datos[2] == "ADMIN":

                while True:

                    print("\n===== Sistema Admin =====")
                    print("1. Registrar usuario")
                    print("2. Listar usuarios")
                    print("3. Buscar usuario")
                    print("4. Modificar usuario")
                    print("5. Eliminar usuario")
                    print("6. Cerrar sesión")

                    opcio = input("Ingresar Opción: ")

                    if opcio == "1":

                        usuario = input("Usuario: ")
                        password = input("Password: ")
                        tipo = input("Tipo (1 ADMIN / 2 USER): ")

                        u = Usuario(usuario=usuario, password=password, tipo_usuario=tipo)
                        u.guardar()

                        print("Usuario creado")

                    elif opcio == "2":

                        u = Usuario()
                        lista = u.listar()

                        for x in lista:
                            print(x)

                    elif opcio == "3":

                        id = input("ID: ")
                        u = Usuario(id=id)

                        print(u.buscar())

                    elif opcio == "4":

                        id = input("ID: ")
                        usuario = input("Nuevo usuario: ")
                        password = input("Nueva password: ")
                        tipo = input("Nuevo tipo: ")

                        u = Usuario(id, usuario, password, tipo)
                        u.modificar()

                        print("Modificado")

                    elif opcio == "5":

                        id = input("ID: ")

                        u = Usuario(id=id)
                        u.eliminar()

                        print("Eliminado")

                    elif opcio == "6":
                        break

            else:

                while True:

                    print("\n===== MENU USER =====")
                    print("Usuario:", datos[1])
                    print("Tipo:", datos[2])
                    print("1. Cerrar sesión")

                    op = input("Opción: ")

                    if op == "1":
                        break

        else:
            print("Usuario o contraseña incorrectos")

    elif opcion == "2":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
        