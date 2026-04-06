# Cadena literal
# Las cadenas son secuencias de caracteres, pueden incluir letras, números, símbolos, y se colocan entre comillas simples o dobles. Por ejemplo:

print("Esta es una cadenas de caracteres.")

# Concatenar cadenas y variables con la función print

nombre = "Marcelo"
print("Me llamo", nombre)

# Otra manera es concatenando el contenido con la ayuda de +.

nombre = "Marcelo"
print("Mi nombre es "+ nombre)

# Conversión de tipos (Type Casting) o Conversión de tipo explícito

print("¿Cuántas vocales hay? " + 5) 
#ERROR: TypeError: can only concatenate str (not "int") to str
print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 5

# Podemos hacer la conversión también de cadena a número, por ejemplo:

tiempo_preparacion = 1
tiempo_horneado = "2"
tiempo_total = tiempo_preparacion + tiempo_horneado 
#ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'
tiempo_total = tiempo_preparacion + int(tiempo_horneado) #Imprime: 3

# Cadenas »f» (Interpolación de cadenas literal)

nombre = "Marcelo"
edad = 29
print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")


'''
string.format()
Antes de que se introdujeran las cadenas “f”, esta misma funcionalidad 
se lograba con el método .format(). Para usar este método, escribimos 
la cadena completa y colocamos llaves ({}) en los espacios en los que q
ueremos desplegar el valor de la variable. Después invocamos al método format
y pasamos las variables como argumentos en el orden que debieran llenarse los
parámetros {}. Por ejemplo:
'''

nombre = "Marcelo"
edad = 29
print("Mi nombre es {} y tengo {} años de edad.".format(nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.
print("Tengo {} años de edad y mi nombre es {}".format(edad, nombre))

#Imprime: Tengo 29 años de edad y mi nombre es Marcelo 

# %-formatting
'''
Quizás en algún código tepuedas topar con un método
que se utilizaba antes deque existiera las formas vistas 
antes de interpolación. En lugar 
de utilizar llaves, se utiliza el 
símbolo % para indicar un parámetro; %s para indicar una cadena y %d para 
indicar un número. Una vez establecida la cadena, se coloca de nuevo % para separar el
texto de las variables que serán interpoladas. Por ejemplo:
'''

nombre = "Marcelo"
edad = 29
print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.