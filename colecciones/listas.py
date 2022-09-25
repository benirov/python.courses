#lista- las listas pueden tener cualquier tipo de datos
nombres = ["Juan", "Katrina", "Alejandra", "Dayry"]
print(nombres[0:2])

#largo de una lista
print(len(nombres))

#agregar un elemento
nombres.append("Jesus")
print(nombres)

#agregar un elemento en una posicion especifica(esto no borra el elemento, solo agrega uno nuevo en la posicion que se necesite)
nombres.insert(1, "Keila")
print(nombres)

#remover elementos
nombres.remove('Keila')
print(nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)


#Eliminar un indice
del nombres[0]
print(nombres)

#Eliminar elementos de la lista
nombres.clear()
print(nombres)

#Eliminar la lista de memoria
del nombres
print(nombres)