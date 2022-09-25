numero = int(input("escribe mes del año(1 a 12): ")) 
mes = None
if numero == 1 or numero == 2 or numero == 12:
    mes = "Invierno"
elif numero == 3 or numero == 4 or numero == 5:
    mes = "Primavera"
elif numero == 6 or numero == 7 or numero == 8:
    mes = "Verano"
elif numero == 9 or numero == 10 or numero == 11:
    mes = "otoño"
else:
    mes = "Fuera de rango"

print(f'para el mes {numero} la estaciòn es {mes}')