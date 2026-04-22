import os
# Funciones básicas practica 2

#----------------------------Ejercicio 1-------------------------------
# Calcula experiencia
def multiplica_por_2(num):
    for i in range(num + 1):
        result = []
        result.append(i * 2)
result1 = multiplica_por_2(5)
print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]

#----------------------------Ejercicio 2-------------------------------
# Analiza publicaciones
def suma_y_resta(list):
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma: {suma}  | resta : {resta}")
# Imprime: 235 y retorna: 5

#----------------------------Ejercicio 3-------------------------------
# Puntaje ajustado
sumatoria_menos_longitud([10, 5, 3, 7])
# Suma total = 25, longitud = 4, debe retornar: 21

#----------------------------Ejercicio 4-------------------------------
# Ajusta visualizaciones
valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []

#----------------------------Ejercicio 5-------------------------------
# Genera precio fijo
valor_multiplicado_longitud(5, 2)
# Debe retornar: [10, 10]

valor_multiplicado_longitud(7, 5)
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
        multiplica_por_2()
    elif opcion == "2":
        ()
    elif opcion == "3":
        ()
    elif opcion == "4":
        ()
    elif opcion == "5":
        ()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")