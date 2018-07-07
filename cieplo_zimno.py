import random

gracz_x = random.randrange(1,11)
gracz_y = random.randrange(1,11)

skarb_x = random.randrange(1,11)
skarb_y = random.randrange(1,11)

print(f'debug: gracz {gracz_x}, {gracz_y}')
print(f'debug: skarb {skarb_x}, {skarb_y}')

krok = input('''
Szukasz skarbu na planszy 10x10
Podaj w którą stronę idziesz:
[l]ewo
[p]rawo
[g]ora
[d]ol
wyjdziesz poza plansze to zginiesz
''')
print(krok)

znaleziony = False

if gracz_x == skarb_x and gracz_y == skarb_y:
    znaleziony = True

poza_plansza = False
if gracz_x < 1 or gracz_x > 10 or gracz_y <1 or gracz_y >10:
    poza_plansza == False

ruch = None

while (not znaleziony) and (not poza_plansza):
    print(f'debug: gracz {gracz_x}, {gracz_y}')
    print(f'debug: skarb {skarb_x}, {skarb_y}')
    if krok == 'l':
        gracz_x -= 1
    if krok == 'p':
        gracz_x += 1
    if krok == 'g':
        gracz_y += 1
    if krok == 'd':
        gracz_y -= 1
    krok = input('Podaj w którą stronę idziesz:')

    if gracz_x == skarb_x and gracz_y == skarb_y:
        znaleziony = True

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        poza_plansza = True

if znaleziony:
    print('znalazles skarb')
if poza_plansza:
    print('spadles z planszy')

