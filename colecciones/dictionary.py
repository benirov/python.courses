#dict (key, value)
dictionary = {
    "Python" :"programming languaje",
    "JSON" : "JavaScript Object Notation",
    "PHP": "Hypertext Preprocessor"}
print(dictionary)

#largo de una tupla
print(len(dictionary))

# acceder a un elemento
print(dictionary['Python'])

# acceder a un elemento(otra forma)
print(dictionary.get('JSON'))

# modificar elemento
dictionary['Python'] = 'Programming Languaje'
print(dictionary)

# recorrer los elementos del diccionario
for code, value in dictionary.items():
    print(code, value)


# recorrer los elementos del diccionario(solo keys)
for key in dictionary.keys():
    print(key)


# recorrer los elementos del diccionario(solo values)
for value in dictionary.values():
    print(value)

#comprobar existencia
print('Python' in dictionary)
print('js' in dictionary)

#agregar elementos
dictionary["PK"] = 'Primary key'
print(dictionary)

#remover elementos
dictionary.pop("PK")
print(dictionary)