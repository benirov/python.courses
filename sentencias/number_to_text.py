numero = int(input("escribe un numero entre 1 y 3: ")) 
numerotexto = ''
if numero == 1:
    numerotexto = "numero 1"
elif numero == 2:
    numerotexto = "numero 2"
elif numero == 3:
    numerotexto = "numero 3"
else:
    numerotexto = "Fuera de rango"

print(f'{numerotexto}')