x = [[1, 2, 3], [4, 5, 6]]
print(x)

a = [1, 2, 3]
b = [4, 5, 6]

x = [a, b]
print(x[0][2])

c = a

c.append(6)

assert a == [1,2,3,6]

d = b.copy()
d.append(7)

assert d == [4,5,6,7]
assert b == [4,5,6]

print(x)
y = x.copy()



print(y)

