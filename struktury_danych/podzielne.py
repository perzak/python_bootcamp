lista = []
podz_3 = 0
podz_5 = 0

for i in range(101):
    lista.append(i)
print(lista)
print(f'Liczby podzielne przez 3 lub 5 to:')
for el in lista:
    if el % 3 == 0 or el % 5 ==0:
        print(el)
    if el % 3 == 0:
        podz_3 +=1
    if el % 5 == 0:
        podz_5 +=1

print(f'podzielnych przez 3 jest {podz_3} a podzielnych przez 5 jest {podz_5}')