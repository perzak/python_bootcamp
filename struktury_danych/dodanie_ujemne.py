lista = [2,4,-5,-5,-3,-7,-2,-5,-7,3,5,54,435]
dodatnie = 0
ujemne = 0
for i in lista:
    if i > 0:
        dodatnie +=1
    elif i < 0:
        ujemne +=1
print(f'na liscie mamy {dodatnie} dodatnik i {ujemne} ujemnych')