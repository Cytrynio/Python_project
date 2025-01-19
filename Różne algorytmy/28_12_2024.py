def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
#

def anagram(word1,word2):
    if sorted(word1) == sorted(word2):
        print("true")
    else:
        print("false")

def pierwsze(zakres):
    l_pierwsze = []
    for num in range(1, zakres):
        if all(num % j != 0 for j in range(2, int(num ** 0.5) + 1)):
            l_pierwsze.append(num)
    return l_pierwsze

print(pierwsze(100))