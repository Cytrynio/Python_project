def decorator(func):
    def wrapper():
        print("------")
        func()
        print("------")
    return wrapper()

def hello():
    print("Hello World")


hello = decorator(hello)


@decorator
def witaj():
    print("Witaj Świecie")

import string

def licz_litery(slowo):
    """Funkcja liczy wystąpienia każdej litery w podanym słowie."""
    alphabet = string.ascii_lowercase
    letter_count = {letter: 0 for letter in alphabet}

    for letter in slowo.lower():  # Konwertujemy na małe litery, aby uwzględniać różne przypadki
        if letter in letter_count:
            letter_count[letter] += 1

    return {letter: count for letter, count in letter_count.items() if count > 0}

# Przykład użycia
slowo = "abrakadabra"
wynik = licz_litery(slowo)
print(wynik)


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j +1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return lista

x= [1,43,5,6,3,2,5,4,22]

print(bubble_sort(x))
