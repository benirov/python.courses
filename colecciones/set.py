#set- un set es una coleccion en donde sus elementos no tienen orden, sus elementos pueden editarse, no soporta elementos duplicados
planets = {"Venus", "Marte", "Mercurio"}
print(planets)

#largo de una tupla
print(len(planets))

#saber si existe un elemento
print('Marte' in planets)


#agregar elemento
planets.add("Heart")
print(planets)

#no se pueden repetir elementos
planets.add("Heart")
print(planets)

#eliminar elementos
planets.remove("Heart")
print(planets)


# limpiar set
planets.clear()
print(planets)

# Eliminar set
del planets
print(planets)

