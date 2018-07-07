komunikat = 'podaj kolejna liczbe lub wpisz [koniec]: '
res = input(komunikat)
if res != 'koniec':
    max = int(res)
    min = int(res)
else:
    min = '"nie podales zadnej liczby"'
    max = '"nie podales zadnej liczby"'

while res != 'koniec':
    res = int(res)

    if res > max:
        max = res
    if res < min:
        min = res

    res = input('podaj kolejna liczbe lub wpisz [koniec]: ')

print(f'najwieksza z podanych liczb to {max}')
print(f'najniejsza z podanych liczb to {min}')