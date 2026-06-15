"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).

def ejercicio1():
    for nivel in range(0, 101):
        print(nivel)


# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).

def ejercicio2():
    for n in range(2, 501, 2):
        print(n)


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime 🔥
# - Si es divisible por 10, imprime 💀
# ¡Cuidado con la prioridad en tus condicionales!

def ejercicio3():
    for i in range(1, 101):
        if i % 10 == 0:
            print("💀")
        elif i % 5 == 0:
            print("🔥")


# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.

def ejercicio4():
    sumatotal = 0

    for num in range(1, 500001):
        if num % 2 == 0:
            sumatotal += num

    print(f"La suma total de los números pares de 500,000 es: {sumatotal}")


# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.

def ejercicio5():
    for temporal in range(2024, -1, -3):
        print(temporal)


# 6. Contador dinámico
# Declara las variables inicio, fin y salto.
# Imprime los números en el rango que sean múltiplos de 'salto'.

def ejercicio6():
    inicio = 3
    fin = 10
    salto = 2

    for multiplos in range(inicio, fin + 1):
        if multiplos % salto == 0:
                print(multiplos)
# ------------------ MENÚ ------------------

while True:
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1.- Ejercicio 1")
    print("2.- Ejercicio 2")
    print("3.- Ejercicio 3")
    print("4.- Ejercicio 4")
    print("5.- Ejercicio 5")
    print("6.- Ejercicio 6")
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
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")