
#----------------------------------parte 1---------------------------------------------------

# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600
print(puntajes)


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"
print(streamers)


# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}

eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)


# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

ubicacion[0]["latitud"] = "40.712776"
print(ubicacion)

#------------------------------------Parte 2 --------------------------------------

def iterar_diccionario(lista):
    for streamers in lista:
        print(f"nombre : {streamers['nombre']} seguidores : {streamers['seguidores']}")


iterar_diccionario(streamers)

def obtener_valores(clave, lista):
    for item in lista:
        print(item[clave])

obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)


#------------------------------------Parte 3 --------------------------------------


for paises, lista in eventos.items():
    print(f"---{paises.upper()}---")
    for item in lista:
        print(f"{item}")
