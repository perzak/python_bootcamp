lista = [99, 2, 9, 100, 5, 6, 7, 8]

min = lista[0]
max = lista[0]
i_min = 0
i_max = 0

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]
        i_max = i
    if lista[i] < min:
        min = lista[i]
        i_min = i

print(min, max)

lista[i_max] = min
lista[i_min] = max

print(lista)

for i in lista:
    print(i)
