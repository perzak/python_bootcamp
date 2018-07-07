# napis = input("Podaj napis: ")
# licznik = 0
#
# for i in napis:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
#         licznik += 1
#
# print(napis)
# print(licznik)


napis = input("Podaj napis: ")
licznik = 0
samogloski = "aeiouy"

for i in napis:
    if i in "aeiouy":
        licznik += 1
print(napis)
print(licznik)

a = napis.count("a")
e = napis.count("e")
i = napis.count("i")
o = napis.count("o")
u = napis.count("")
y = napis.count("u")

print(f"")

