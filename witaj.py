x = int(input('Podaj pozycje gracza X: '))
y = int(input('Podaj pozycje gracza Y: '))

if x < 11:
    x_poz = 'left'
elif x > 89:
    x_poz = 'right'
else:
    x_poz = ''

if y < 11:
    y_poz = 'top'
elif y > 89:
    y_poz = 'bottom'
else:
    y_poz = ''

if x_poz and y_poz:
    print (x_poz, y_poz, 'corner')
elif y_poz or x_poz:
    print(x_poz, y_poz, 'edge')
else:
    print('center')