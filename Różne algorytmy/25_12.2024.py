import string

liczby_parzyste = [x for x in range(1,101) if x % 2 == 0]

print(liczby_parzyste)

suma_liczb = [3, 5, 7, 9, 11]

number = 0

for i in suma_liczb:
    number += i

print(sum(suma_liczb))
print(number)


najwieksze = [12, 45, 7, 34, 100, 24]

maximum = 0
for i in najwieksze:
    if i > maximum:
        maximum= i
    else:
        pass

print(maximum)
print(max(najwieksze))


lista =  ["jabłko", "gruszka", "śliwka", "banan"]

print(lista[::-1])


podzielne = [10, 21, 33, 40, 55, 60, 77]

podzielne_5 = [i for i in podzielne if i % 5 ==0]

print(podzielne_5)


# Anagramy Napisz program, który sprawdzi, czy dwa dane słowa (np. "listen" i "silent")
# są anagramami (czyli mają te same litery w różnych kolejnościach).

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print("It's anagram")
else:
    print("Not anagram")


slowo="abrakadabra"

alphabet = string.ascii_lowercase
letter_count = {letter: 0 for letter in alphabet}


for letter in slowo:
    if letter in letter_count:
        letter_count[letter] += 1

print(letter_count)




def tabliczka_mnozenia():
    result = []
    for i in range(1,6):
        wiersz = []
        for j in range(1,6):
            wiersz.append(i*j)
        result.append(wiersz)
    return result

tabliczka = tabliczka_mnozenia()
for wiersz in tabliczka:
    print(wiersz)


lista1 = [1, 2, 2, 3, 4, 4, 5]
lista2 = []
for i in lista1:
    if i not in lista2:
        lista2.append(i)

print(lista2)