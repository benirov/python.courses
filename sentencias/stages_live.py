numero = int(input("escribe tu edad :")) 
mesage = None
if 0 <= numero  < 10:
    mesage = "infancia"
elif 10 <= numero < 20:
    mesage = "adolescencia"
elif 20 <=  numero < 30:
    mesage = "madurez"
else:
    mesage = "Fuera de rango"

print(f'Tu etapa de vida es {mesage}')