# 📖 Crear diccionarios
'''
Hasta ahora hemos visto dos tipos de conjuntos en Python:
Listas y Tuplas. Las listas las inicializamos con corchetes:
[ ], las tuplas las inicializamos con paréntesis: ( ), y ahora 
los diccionarios los serán con llaves: { }. Veamos juntos el
siguiente ejemplo:
'''

estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
estudiante["nombre"] = "Vicente"
estudiante["nombre"] = "Dany"
# Imprimir el nombre de estudiante 
print (estudiante["nombre"])

# Diccionario de paises
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Peru"
paises["ARG"] = "Argentina"


# Verificar la existencia de una clave

if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"
    
# Remover valores
print(paises)

valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

print(f"Valor Removido : {valor_removido}")
print(paises)

# Sintaxis multi-línea 

pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}

#Puede ser escrito de esta manera:
pintor = {
    "nombre": "Frida Kahlo",
    "pais": "México",
    "fecha_nacimiento": "6 de julio de 1907"
}

# Diccionarios anidados

'''
Como mencionamos anteriormente, los valores que podemos
utilizar para los diccionarios pueden contener listas,
tuplas e inclusive otros diccionarios.
'''

escuela = {
    "nombre": "Coding Dojo LATAM",
    "profesores": [
        {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
        {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
        {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
    ]
}