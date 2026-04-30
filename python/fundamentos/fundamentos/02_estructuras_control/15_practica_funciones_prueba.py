'''
Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
Crear una función que reciba un número entero y determine si es par o impar.
Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.

'''

#---------------------------------------ejercicio 1---------------------------------
def numeroMayor(lista):
    mayor = max(lista)
    menor = min(lista)
    print(f"El número mayor es {mayor}")
    print(f"El número menor es {menor}")


def ejercicio1():
    limite = int(input("Ingresa cantidad de números: "))
    lista = []

    for i in range(limite):
        num = int(input(f"Ingrese número {i+1}: "))
        lista.append(num)

    numeroMayor(lista)
        
#---------------------------------------ejercicio 2---------------------------------
def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador += 1
    print("Vocales:", contador)


def ejercicio2():
    texto = input("Texto: ")
    contar_vocales(texto)


#---------------------------------------ejercicio 3---------------------------------
def filtrar_nombres(lista):
    for nombre in lista:
        if len(nombre) > 5:
            print(nombre)


def ejercicio3():
    nombres = []
    n = int(input("Cantidad de nombres: "))

    for i in range(n):
        nombres.append(input("Nombre: "))

    filtrar_nombres(nombres)


#---------------------------------------ejercicio 4---------------------------------
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    print("Promedio:", promedio)

    if promedio >= 4.0:
        print("Aprueba")
    else:
        print("Reprueba")


def ejercicio4():
    notas = []
    n = int(input("Cantidad de notas: "))

    for i in range(n):
        notas.append(float(input("Nota: ")))

    calcular_promedio(notas)


#---------------------------------------ejercicio 5---------------------------------
def aplicar_descuento(precios):
    for precio in precios:
        nuevo = precio * 0.9
        print(f"Original: {precio} - Nuevo: {nuevo}")


def ejercicio5():
    precios = []
    n = int(input("Cantidad de precios: "))

    for i in range(n):
        precios.append(float(input("Precio: ")))

    aplicar_descuento(precios)


#---------------------------------------ejercicio 6---------------------------------
def es_par(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")


def ejercicio6():
    num = int(input("Número: "))
    es_par(num)


#---------------------------------------ejercicio 7---------------------------------
def contar_mayores(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    print("Mayores de edad:", contador)


def ejercicio7():
    edades = []
    n = int(input("Cantidad de personas: "))

    for i in range(n):
        edades.append(int(input("Edad: ")))

    contar_mayores(edades)


#---------------------------------------ejercicio 8---------------------------------
def contar_palabra(lista, palabra):
    contador = 0
    for p in lista:
        if p == palabra:
            contador += 1
    print("Se repite:", contador)


def ejercicio8():
    palabras = []
    n = int(input("Cantidad de palabras: "))

    for i in range(n):
        palabras.append(input("Palabra: "))

    buscar = input("Palabra a buscar: ")
    contar_palabra(palabras, buscar)


#---------------------------------------ejercicio 9---------------------------------
def positivos(lista):
    nueva = []
    for num in lista:
        if num > 0:
            nueva.append(num)
    print(nueva)


def ejercicio9():
    lista = []
    n = int(input("Cantidad de números: "))

    for i in range(n):
        lista.append(int(input("Número: ")))

    positivos(lista)


#---------------------------------------ejercicio 10---------------------------------
def bajo_stock(productos):
    for p in productos:
        if p["stock"] < 5:
            print(p["nombre"])


def ejercicio10():
    productos = []
    n = int(input("Cantidad de productos: "))

    for i in range(n):
        nombre = input("Nombre: ")
        stock = int(input("Stock: "))
        productos.append({"nombre": nombre, "stock": stock})

    bajo_stock(productos)


