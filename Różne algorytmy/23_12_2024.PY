# Największa liczba
import string


numbers = [12, 45, 78, 34, 89, 23, 67]

def najwieksza(lista):
    return max(lista)

print(najwieksza(numbers))


words = ["Python", "is", "fun"]

def odwroc(text):
    return  text[::-1]

print(odwroc(words))


numbers_1 = [1, 2, 2, 3, 4, 4, 5]

def remove_dupli(lista):
    new_list = []
    for i in lista:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_dupli(numbers_1))

sentence = "Ala ma kota i lubi programować"
def samogloski(sent):
    num = 0
    vowels = "AEIOUaeiou"
    for char in sent:
        if char in vowels:
            num += 1
    return num

print(samogloski(sentence))

word = "kajak"

def palindrome_checker(text):
    if text == text[::-1]:
        print("It's a palindrome")
    else:
        print("It''s not a palindrome")

palindrome_checker(word)


# Tabliczka mnożenia

def tabliczka_mnożenia():
    result = []
    for i in range(1,11):
        wiersz = []
        for j in range(1,11):
            wiersz.append(i * j)
        result.append(wiersz)
    return result

tabliczka = tabliczka_mnożenia()
for wiersz in tabliczka:
    print(wiersz)


def pierwsze():
    liczby = []
    for i in range(2,101):
        czy_pierwsza = True
        for dzielnik in range(2,int(i**0.5) + 1):
            if i % dzielnik == 0:
                czy_pierwsza = False
                break
        if czy_pierwsza:
            liczby.append(i)
    return liczby

print(pierwsze())


text = "programowanie"

alph = string.ascii_lowercase
letter_count = {letter: 0 for letter in alph}

for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1

print(letter_count)


original_dict = {"a": 1, "b": 2, "c": 3}

reversed_dict  = {value: key for key,value in original_dict.items()}

print(reversed_dict)


wynik = [i for i in range(1,21) if i % 2 == 0 ]

print(wynik)