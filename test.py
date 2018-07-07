dni = 0
temperatura = 0
while dni < 7:
    x = int(input('podaj temperature '))
    dni += 1
    temperatura += x

print(f'srednia temperatura z 7 dni = {temperatura/dni}')