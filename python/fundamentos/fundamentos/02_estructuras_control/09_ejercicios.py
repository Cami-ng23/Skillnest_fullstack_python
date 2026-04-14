'''
Guía de Ejercicios: Lógica Fundamental
I. Interacción y Condicionales (Básico)
1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$).
El programa debe imprimir los primeros $n$ números pares positivos.
2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento.
Calcula su edad y muestra si es mayor de edad (18+).
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada.
Si el total supera los $100, aplica un 15% de descuento.
Muestra el subtotal, el descuento aplicado y el total final.
4. Clasificador de Números
Pide un número al usuario e indica si es:
Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
II. Iteraciones y Bucles (Intermedio)
5. Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12,
pero solo muestra los resultados que sean múltiplos de 3.
6. Sumatoria con Centinela
Crea un programa que pida números continuamente y los sume.
El ciclo debe terminar cuando el usuario ingrese un número negativo.
Al final, muestra la suma total (sin incluir el negativo).
7. Contador de Vocales
Pide al usuario una frase o palabra. Utiliza un bucle para recorrer 
la cadena y contar cuántas vocales tiene en total.
8. Validación de Contraseña
Define una contraseña en una variable. Pide al usuario que 
la intente adivinar. Tienes un máximo de 3 intentos;
si falla los 3, bloquea el acceso.
III. Manejo de Arreglos / Listas (Avanzado)
9. Registro de Nombres
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres.
Guárdalos en el arreglo y, al final,
imprímelos en orden inverso al que fueron ingresados.
10. Promedio de Notas
Solicita al usuario cuántas notas desea ingresar. 
Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio,
la nota más alta y la más baja.
11. Filtro de Arreglos
Dado un arreglo de números generado por el usuario,
crea un nuevo arreglo que contenga solo los números que sean mayores a 50.
Muestra ambos arreglos.
12. Buscador de Elementos
Crea una lista de 10 ciudades. Pide al usuario que 
ingrese el nombre de una ciudad y el programa debe decir si 
la ciudad se encuentra en la lista y en qué índice (posición) está.
IV. Retos de Lógica Combinada
13. Simulación de Inventario
Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
14. Generador de Lista de Compras
Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
15. Análisis de Temperaturas
Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

'''

# ------------------ EJERCICIO 1 ------------------
'''
Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$).
El programa debe imprimir los primeros $n$ números pares positivos.
'''

def ejercicio1():
    n = int(input("¿Cuántos números pares deseas ver? "))
    pares = []

    for i in range(1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i)

    print("Números pares:", pares)


# ------------------ EJERCICIO 2 ------------------
'''
Verificador de Edad y Acceso
Pide al usuario su año de nacimiento.
Calcula su edad y muestra si es mayor de edad (18+).
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
'''

def ejercicio2():
    anio = int(input("Pon año de nacimiento: "))
    edad = 2026 - anio

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print(f"Te faltan {18 - edad} años para ser mayor de edad")


# ------------------ EJERCICIO 3 ------------------
'''
Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada.
Si el total supera los $100, aplica un 15% de descuento.
Muestra el subtotal, el descuento aplicado y el total final.
'''

def ejercicio3():
    precio = float(input("Ingresar precio: "))
    cantidad = int(input("Ingresar cantidad: "))

    subtotal = precio * cantidad

    if subtotal >= 100:
        descuento = subtotal * 0.15
    else:
        descuento = 0

    total = subtotal - descuento

    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")
    print(f"Total: {total}")


# ------------------ EJERCICIO 4 ------------------
'''
Clasificador de Números
Pide un número al usuario e indica si es:
Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
'''

def ejercicio4():
    num = int(input("Ingresar número: "))

    if num == 0:
        print("Cero")
    elif num > 0:
        if num % 2 == 0:
            print("Positivo-Par")
        else:
            print("Positivo-Impar")
    else:
        if num % 2 == 0:
            print("Negativo-Par")
        else:
            print("Negativo-Impar")


# ------------------ EJERCICIO 5 ------------------
'''
Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12,
pero solo muestra los resultados que sean múltiplos de 3.
'''

def ejercicio5():
    num = int(input("Ingresar número: "))

    for i in range(1, 13):
        resultado = num * i
        if resultado % 3 == 0:
            print(f"{num} x {i} = {resultado}")


# ------------------ EJERCICIO 6 ------------------
'''
Sumatoria con Centinela
Crea un programa que pida números continuamente y los sume.
El ciclo debe terminar cuando el usuario ingrese un número negativo.
Al final, muestra la suma total (sin incluir el negativo).
'''

def ejercicio6():
    suma = 0

    while True:
        num = int(input("Ingresa un número (negativo para terminar): "))
        if num < 0:
            break
        suma += num

    print("Suma total:", suma)


# ------------------ EJERCICIO 7 ------------------
'''
Contador de Vocales
Pide al usuario una frase o palabra. Utiliza un bucle para recorrer 
la cadena y contar cuántas vocales tiene en total.
'''

def ejercicio7():
    texto = input("Ingrese una frase o palabra: ")
    contador = 0

    for letra in texto:
        if letra.lower() in "aeiou":
            contador += 1

    print("Cantidad de vocales:", contador)


# ------------------ EJERCICIO 8 ------------------
'''
Validación de Contraseña
Define una contraseña en una variable. Pide al usuario que 
la intente adivinar. Tienes un máximo de 3 intentos;
si falla los 3, bloquea el acceso.
'''

def ejercicio8():
    contrasena = "Programacion"
    intentos_max = 3

    for intento in range(1, intentos_max + 1):
        ingreso = input("Ingrese la contraseña: ")
        
        if ingreso == contrasena:
            print("Acceso concedido")
            return
        else:
            print("Contraseña incorrecta")
    
    print("Acceso bloqueado")


# ------------------ EJERCICIO 9 ------------------
'''
Registro de Nombres
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres.
Guárdalos en el arreglo y, al final,
imprímelos en orden inverso al que fueron ingresados.
'''

def ejercicio9():
    nombres = []

    for i in range(5):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)

    print("Nombres en orden inverso:")
    for nombre in reversed(nombres):
        print(nombre)


# ------------------ EJERCICIO 10 ------------------
'''
Promedio de Notas
Solicita al usuario cuántas notas desea ingresar. 
Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio,
la nota más alta y la más baja.
'''

def ejercicio10():
    cantidad = int(input("¿Cuántas notas desea ingresar? "))
    notas = []

    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print("Promedio:", promedio)
    print("Nota más alta:", nota_max)
    print("Nota más baja:", nota_min)


# ------------------ EJERCICIO 11 ------------------
'''
Filtro de Arreglos
Dado un arreglo de números generado por el usuario,
crea un nuevo arreglo que contenga solo los números que sean mayores a 50.
Muestra ambos arreglos.
'''

def ejercicio11():
    cantidad = int(input("¿Cuántos números desea ingresar? "))
    numeros = []

    for i in range(cantidad):
        num = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)

    mayores_50 = [n for n in numeros if n > 50]

    print("Arreglo original:", numeros)
    print("Números mayores a 50:", mayores_50)


# ------------------ EJERCICIO 12 ------------------
'''
Buscador de Elementos
Crea una lista de 10 ciudades. Pide al usuario que 
ingrese el nombre de una ciudad y el programa debe decir si 
la ciudad se encuentra en la lista y en qué índice (posición) está.
'''

def ejercicio12():
    ciudades = ["Madrid", "París", "Londres", "Roma", "Berlín",
                "Lisboa", "Santiago", "Viena", "Praga", "Valparaiso"]

    busqueda = input("Ingrese el nombre de una ciudad: ")

    ciudades_lower = [c.lower() for c in ciudades]

    if busqueda.lower() in ciudades_lower:
        indice = ciudades_lower.index(busqueda.lower())
        print(f"La ciudad '{ciudades[indice]}' está en la posición {indice}.")
    else:
        print("La ciudad NO se encuentra en la lista.")


# ------------------ EJERCICIO 13 ------------------
'''
Simulación de Inventario
Crea dos arreglos: uno para nombres_productos y otro para precios. 
Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada:
Producto: [Nombre] - Precio: $[Valor].
'''

def ejercicio13():
    nombres_productos = []
    precios = []

    for i in range(3):
        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        precio = float(input(f"Ingrese el precio de {nombre}: $"))
        
        nombres_productos.append(nombre)
        precios.append(precio)

    print("\nInventario:")
    for i in range(3):
        print(f"Producto: {nombres_productos[i]} - Precio: ${precios[i]:.2f}")


# ------------------ EJERCICIO 14 ------------------
'''
14. Generador de Lista de Compras
Usa un bucle while para que el usuario 
agregue artículos a una lista de compras. 
El proceso termina cuando el usuario escribe 
"terminar". Al final, muestra la lista ordenada 
alfabéticamente.
'''

def ejercicio14():
    lista = []

    while True:
        item = input("Articulo (o `terminar`)")
        if item.lower() == "terminar":
            break
        lista.append(item)
    print(f"Ordenada:{sorted(lista)}")
    # sorted ordena la lista 

# ------------------ EJERCICIO 15 ------------------
'''
15. Análisis de Temperaturas
Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

'''

def ejercicio15():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    diasSuperior = []
    total = 0
    baja = 100
    diaBaja = ""
    cant = 0

    while cant < 7:
        temps = float(input(f"Ingrese temperatura del día {dias[cant]}: "))
        total += temps 
        
        if temps < baja and temps < 25:
            baja = temps 
            diaBaja = dias[cant]
        
        if temps > 25:
            diasSuperior.append(dias[cant])
        
        cant += 1  # 

    promedio = total / 7

    print(f"Promedio de temperatura: {promedio}")
    print(f"Día más frío bajo 25°: {diaBaja} con {baja}°")
    print(f"Días con temperatura superior a 25°: {diasSuperior}")


# ------------------ MENÚ ------------------
while True:
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1.- Ejercicio 1")
    print("2.- Ejercicio 2")
    print("3.- Ejercicio 3")
    print("4.- Ejercicio 4")
    print("5.- Ejercicio 5")
    print("6.- Ejercicio 6")
    print("7.- Ejercicio 7")
    print("8.- Ejercicio 8")
    print("9.- Ejercicio 9")
    print("10.- Ejercicio 10")
    print("11.- Ejercicio 11")
    print("12.- Ejercicio 12")
    print("13.- Ejercicio 13")
    print("14.- Ejercicio 14")
    print("15.- Ejercicio 15")
    print("0.- Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        ejercicio7()
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()
    elif opcion == "11":
        ejercicio11()
    elif opcion == "12":
        ejercicio12()
    elif opcion == "13":
        ejercicio13()
    elif opcion == "14":
        ejercicio14()
    elif opcion == "15":
        ejercicio15()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")