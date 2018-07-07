i = 0
lista = []
while i < 10:
    lista.append(int(input('Podaj liczbe calkowita: ')))
    i += 1

sr = sum(lista)/len(lista)

print(f'Srednia z {len(lista)} elementów listy to: {sr}')







