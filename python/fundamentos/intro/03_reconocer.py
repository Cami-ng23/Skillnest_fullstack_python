"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""

import random  
# Importación de la librería 'random' para trabajar con valores aleatorios


nombre = "Frida Kahlo"  
# Creación de una variable de tipo string (cadena de texto)

print(type(nombre))  
# type(): función que devuelve el tipo de dato de una variable

print(len(nombre))  
# len(): función que devuelve la cantidad de caracteres de una cadena


edad = 25  
# Creación de una variable de tipo entero (int)


if edad < 18:  
    # Estructura condicional: evalúa si la edad es menor a 18
    print("Eres menor de edad.")  

elif edad == 18:  
    # Se ejecuta si la condición anterior no se cumple y edad es exactamente 18
    print("Tienes 18 años.")  

else:  
    # Se ejecuta si ninguna de las condiciones anteriores se cumple
    print("Eres mayor de edad.")  


frutas = ["manzana", "pera", "fresa"]  
# Lista: colección de elementos ordenados y modificables

print(frutas[0])  
# Acceso a un elemento de la lista por índice (posición 0)

frutas[0] = "banana"  
# Modificación de un elemento en la lista

frutas.append("uva")  
# append(): agrega un elemento al final de la lista

frutas.remove("pera")  
# remove(): elimina un elemento específico de la lista


dimensiones = (200, 50)  
# Tupla: colección ordenada pero INMUTABLE (no se puede modificar)

print(dimensiones[0])  
# Acceso a un elemento de la tupla


persona = {
    "nombre": "Carlos",
    "edad": 30
}  
# Diccionario: estructura de datos con pares clave:valor

print(persona["nombre"])  
# Acceso a un valor mediante su clave

persona["edad"] = 31  
# Modificación de un valor existente en el diccionario

persona["ciudad"] = "Santiago"  
# Agregar un nuevo par clave:valor

del persona["ciudad"]  
# Eliminar un elemento del diccionario


for i in range(5):  
    # Bucle for: recorre valores desde 0 hasta 4
    if i == 2:
        continue  
        # continue: salta a la siguiente iteración

    if i == 4:
        break  
        # break: detiene completamente el bucle

    print(i)  
    # Imprime el valor de i en cada iteración


contador = 0  
# Inicialización de variable para el bucle while

while contador < 3:  
    # while: se ejecuta mientras la condición sea verdadera
    print(f"while contador es: {contador}")  
    # f-string: permite insertar variables dentro de un string

    contador += 1  
    # Incremento del contador


def saludar_usuario(nombre):  
    # Definición de una función con parámetro
    return f"Hola, {nombre}"  
    # return: devuelve un valor


print(saludar_usuario("Francisca"))  
# Llamada a la función y muestra del resultado