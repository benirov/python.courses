edad = int(input("Introduce tu edad: "))
valorMinimo = 0
valorMaximo = 5

veintes = edad >= 20 and edad < 30
treinta = edad >= 30 and edad < 40

if veintes:
    print(f'dentro de rango (20\'s)')
elif treinta:
    print(f'dentro de rango  (30\'s)')
else:
    print(f'fuera de rango ')