import os
# Funciones básicas practica 2

#----------------------------Ejercicio 1-------------------------------
# Calcula experiencia
def ejercicio1(num):
    for i in range(num + 1):
        result = []
        result.append(i * 2)
result1 = ejercicio1(5)
print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]

#----------------------------Ejercicio 2-------------------------------
# Analiza publicaciones
def ejercicio2(list):
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma: {suma}  | resta : {resta}")
# Imprime: 235 y retorna: 5

#----------------------------Ejercicio 3-------------------------------
# Puntaje ajustado
def suma(lista):
    return sum(lista)

def ejercicio3(lista):
    return suma(lista) - len(lista)

print(ejercicio3([10, 5, 3, 7]))
# 21
# Suma total = 25, longitud = 4, debe retornar: 21

#----------------------------Ejercicio 4-------------------------------
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
    else:
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i *segEle)
        long = len(nuevaLista)
        print(long)
        return nuevaLista
def ejercicio4():
    result1 = valores_multiplicados_segundo([100, 3, 50, 20])
    print(result1)
    print()            
# Imprime: 4 y retorna: [300, 9, 150, 60]
result2 = valores_multiplicados_segundo([100])
print(result2)

valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []

#----------------------------Ejercicio 5-------------------------------
# Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range (0, b):
        multList.append(a * b)
    return multList

def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"Resultado 1: {result1}")
# Debe retornar: [10, 10]
result2 = valor_multiplicado_longitud(7, 5)
print(f"Resultado 2: {result2}")
# Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
    os.system('cls')
    
    # ------------------ MENÚ ------------------
while True:
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1.- Ejercicio 1")
    print("2.- Ejercicio 2")
    print("3.- Ejercicio 3")
    print("4.- Ejercicio 4")
    print("5.- Ejercicio 5")
    print("0.- Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        limpiar_consola()
        ejercicio1()
    elif opcion == "2":
        limpiar_consola()
        ejercicio2()
    elif opcion == "3":
        limpiar_consola()
        ejercicio3()
    elif opcion == "4":
        limpiar_consola()
        ejercicio4()
    elif opcion == "5":
        limpiar_consola()
        ejercicio5()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")