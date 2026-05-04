import os

def ingreso_numeros():
    numeros = []
    for i in range(5):
        num = int(input("Ingresa un número: "))
        numeros.append(num)
    return numeros


def positivos_negativos(numeros):
    for num in numeros:
        if num < 0:
            print("Ingresaste un número negativo:", num)
            return false
    
    print(f"Ingresaste los siguientes numeros :{numeros}")


def limpiar_consola():
    os.system('cls')

# ----------- MENÚ ------------

while True:
    print("\n1. Ingresar números")
    print("2. Verificar")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        numeros = ingreso_numeros()

    elif opcion == "2":
        positivos_negativos(numeros)

    elif opcion == "0":
        break