#tuplas- una tupla siempre guarda el orden de los elementos y ya  no se pueden modificar(inmutabilidad)
companies = ("IBM", "Globant", "Tesla", "Apple")
print(companies)

#largo de una tupla
print(len(companies))

#acceder un elemento
print(companies[2])

#navegacion inversa
print(companies[-1])

#Acceder a un rango
print(companies[0:2])

#iteracion
for company in companies:
    print(company, end=' ') 

#cambiar valores de una tupla

companiesList = list(companies)

companiesList[0] = 'Brave'
companies = tuple(companiesList)
print('\n',companies)

#Eliminar la tupla
del companies
print(companies)