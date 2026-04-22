"""
Funciones básicas 1 - Ejercicios + Variables | Valores + Salida
"""

#----------------------------Ejercicio 1-------------------------------
def total_logros_desbloqueados():
    return 7

print(total_logros_desbloqueados())

# Variables | Valores
#           |
# Salida: 7


#----------------------------Ejercicio 2-------------------------------
def mensajes_en_chat():
    return 2450

# Variables | Valores
#           |
# Salida: 2450


#----------------------------Ejercicio 3-------------------------------
# print(cantidad_de_dias_en_el_anio() + mensajes_en_chat())

# Variables | Valores
#           |
# Salida: Error (NameError)


#----------------------------Ejercicio 4-------------------------------
def temporada_rango_especial():
    return 2022
    return 2021

print(temporada_rango_especial())

# Variables | Valores
#           |
# Salida: 2022


#----------------------------Ejercicio 5-------------------------------
def total_playlists():
    return 12
    print(15)

print(total_playlists())

# Variables | Valores
#           |
# Salida: 12
# el segundo print no se ejecuta


#----------------------------Ejercicio 6-------------------------------
def episodios_serie_favorita():
    print(24)

x = episodios_serie_favorita()
print(x)

# Variables | Valores
# x         | None
# Salida:
# 24
# None


#----------------------------Ejercicio 7-------------------------------
def suma_puntos(a, b):
    print(a + b)

# print(suma_puntos(10, 5) + suma_puntos(4, 3))

# Variables | Valores
# a         | 10 - 4
# b         | 5 - 3
# Salida:
# 15
# 7
# Error (TypeError)


#----------------------------Ejercicio 8-------------------------------
def combinar_tags(tag1, tag2):
    return str(tag2) + str(tag1)

print(combinar_tags("#Verano", "#Diversión"))

# Variables | Valores
# tag1      | #Verano
# tag2      | #Diversión
# Salida: #Diversión#Verano


#----------------------------Ejercicio 9-------------------------------
def conteo_reproducciones_video():
    a = 560000
    print(a)
    if a < 180000:
        return 33
    else:
        return 46
    return 21

print(conteo_reproducciones_video())

# Variables | Valores
# a         | 560000
# Salida:
# 560000
# 46


#----------------------------Ejercicio 10-------------------------------
def duracion_suscripcion(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52

print(duracion_suscripcion(1, 3))
print(duracion_suscripcion(7, 4))
print(duracion_suscripcion(7, 4) + duracion_suscripcion(1, 3))

# Variables | Valores
# a         | 1   | 7
# b         | 3   | 4
# Salida:
# 365
# 12
# 377


#----------------------------Ejercicio 11-------------------------------
def suma_propinas(a, b):
    return a + b
    return 157

print(suma_propinas(3, 4))

# Variables | Valores
# a         | 3
# b         | 4
# Salida: 7


#----------------------------Ejercicio 12-------------------------------
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# Variables | Valores
# horas_de_juego | 150 (global) / 350 (local)
# Salida:
# 150
# 150
# 350
# 150


#----------------------------Ejercicio 13-------------------------------
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# Variables | Valores
# horas_de_juego | 150 / 350
# Salida:
# 150
# 150
# 350
# 150


#----------------------------Ejercicio 14-------------------------------
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
horas_de_juego = mostrar_horas_local()
print(horas_de_juego)

# Variables | Valores
# horas_de_juego | 150 / 350
# Salida:
# 150
# 150
# 350
# 350


#----------------------------Ejercicio 15-------------------------------
def mostrar_seguidores():
    print("Seguidores: 300")
    mostrar_likes()
    print("Finalizando conteo")

def mostrar_likes():
    print("Likes: 120")

mostrar_seguidores()

# Variables | Valores
# Seguidores | 300
# Likes      | 120
# Salida:
# Seguidores: 300
# Likes: 120
# Finalizando conteo


#----------------------------Ejercicio 16-------------------------------
def mostrar_reproducciones():
    print("Reproducciones: 5000")
    a = calcular_incremento()
    print(a)
    return 4

def calcular_incremento():
    print("Incremento calculado:")
    return 1

b = mostrar_reproducciones()
print(b)

# Variables | Valores
# a         | 1
# b         | 4
# Salida:
# Reproducciones: 5000
# Incremento calculado:
# 1
# 4