print('   ', end='')
for x in range(10):
    print(f'{x:^3}', end=' ')
print()
for x in range(10):
    print()
    print (f'{x:<3}', end ='')
    for y in range(10):
        print(f'{x*y:^3}', end=' ')