'''
int	var num = 156;	num = 156
float	var pi = 3.1416;	pi = 3.1416
Imprimir	console.log(num);	print(num)
Verificación de tipo	console.log(typeof(pi));	print(type(pi))
Conversión	N/A. Todos los números son flotantes en JavaScript	num_a_decimal = float(num)
Número aleatorio entre 5 – 10	var rand_num = Math.floor(Math.random() * 6) + 5;	import random
num_aleatorio = random.randint(5,10)
'''

'''
Conversión
Todos los objetos en Python tienen métodos que podemos utilizar para convertir de un tipo de número a otro.
'''
entero_a_decimal = float(123)
decimal_a_entero = int(22.5)
entero_a_complejo = complex(35)
print(entero_a_decimal) #Imprime: 123.0
print(decimal_a_entero) #Imprime: 22
print(entero_a_complejo) #Imprime: (35+0j)

'''
🎲 Número aleatorio
Para generar un número aleatorio importamos la librería random. Puedes ver la documentación oficial de la librería aquí.
'''

import random
num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
print(num_aleatorio) #Imprime el número aleatorio generado


