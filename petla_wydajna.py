komunikat = 'podaj kolejna liczbe lub wpisz [koniec]: '
res = input(komunikat)

# najpierw obsluz wjatkowe sytuacje
if res == 'koniec':
    exit('Nie podales zadnych liczb')

liczba = int(res)
min = liczba
max = liczba

while True:
    res = input(komunikat)
    if res == 'koniec':
        break

    liczba = int(res)
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print(f'najwieksza z podanych liczb to {max}')
print(f'najniejsza z podanych liczb to {min}')