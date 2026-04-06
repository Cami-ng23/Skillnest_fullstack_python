'''
Actividad : Gestor de Inventario '''

'''
1.- Creacion : Crear una lista llamada inventario que contenga lo siguiente
articulos :laptop, raton, monitor , cable hdmi'''

inventario = ["laptop", "raton", "monitor", "cable hdmi" ]
'''
2.- Expansion_ Utiliza el método correspondiente para agregar "Impresora" y teclado mecanico
al final de la lista '''

inventario.append("Impresora")
inventario.append("teclado ")
print(inventario)

''' 
Conteo: Utiliza la función integrada para mostrar cuantos elementos totales hay en la lista '''
print(len(inventario))

''' 4.- Acceso y modificación: Modificaa teclado por teclado mecanico'''
inventario[5] = "teclado mecanico"

''' 5.- Slicing : Crea una nueva lista llamada promoción , debe contener solo los 3 primeros elementos de la
lista articulos '''

promocion = inventario 
print(promocion [:3])
''' 6.- Mostrar la lista de inventario ordenado alfabeticamente.'''
list.sort(inventario )
print(inventario)

'''7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final '''

eliminado = inventario.pop()
print("Articulo")