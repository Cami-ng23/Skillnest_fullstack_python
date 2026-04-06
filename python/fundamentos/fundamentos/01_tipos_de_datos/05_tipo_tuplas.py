tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

# Las tuplas agrupan un conjunto de elementos que pueden contener cualquier tipo de dato.

gato = ("Miu", 5, "persa", False)
print(gato[0]) #Imprime: Miu

# Recuerda que las tuplas son inmutables, por lo que al intentar cambiar el valor de algún índice obtendremos un TypeError:

# gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assign

# A pesar de esto, podemos agregar elementos a las tuplas o hacer slicing.
gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')

# 🧮 Tupla como valores return
# En los próximos capítulos aprenderás sobre funciones, a través de ellas podemos devolver un valor. Pero habrá ocasiones en que necesitemos devolver más de un valor, para esto podemos utilizar una tupla. Esta va a permitir agrupar más de un valor y devolverlos juntos. Por ejemplo, imaginemos que necesitamos una función que te regrese la sumatoria y la multiplicación de dos números:

def suma_multiplicacion(x, y):
    suma = x + y
    multiplicacion = x * y
    return (suma , multiplicacion)

print(suma_multiplicacion(10,5))