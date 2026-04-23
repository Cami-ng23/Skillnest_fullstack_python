datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]



# 1. Cambiar el puntaje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]
datos[2]["puntaje"] = 75
print(datos)


# 2. Imprimir frases
def imprimir(lista):
    for p in lista:
        print(p["nombre"], "obtuvo", p["puntaje"], "puntos")


# 3. Imprimir solo una clave
def mostrar(lista, clave):
    for p in lista:
        print(p[clave])


imprimir(datos)
mostrar(datos, "nombre")
mostrar(datos, "puntaje")
