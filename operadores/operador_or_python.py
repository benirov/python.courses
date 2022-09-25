vacaciones = False
diasDescanso = True
asistir = (vacaciones) or (diasDescanso)

if asistir:
    print(f'Puedes asistir al juego de tu hijo')
else:
    print(f'No puedes asistir al juego de tu hijo')