# Zadanie 2: Kwadraty liczb
# Dany jest zakres liczb od 1 do 10. Użyj list comprehension,
# aby utworzyć listę kwadratów tych liczb.

# for x in range(1,11):
#     print(x**x)
#
wynik = [x**2 for x in range(1,11)]

print(wynik)


words = ["python", "java", "c", "ruby", "javascript"]
# Użyj list comprehension, aby stworzyć listę,
# która zawiera tylko te słowa, które mają więcej niż 4 litery.

slowa = [i for i in words if len(i) >= 4]

print(slowa)


words1 = ["Python", "java", "c", "Ruby", "JavaScript"]

mala_litera = [i.lower() for i in words1]

print(mala_litera)


parorniepar = ["parzysta"if i % 2 == 0 else "nieprzysta" for i in range(1,16)]

print(parorniepar)

dodawanie = [i+i+3 for i in range(1,11)]
print(dodawanie)

original_dict = {"a": 1, "b": 2, "c": 3}
dict_to_list = [value for value in original_dict.values()]

print(dict_to_list)

pierwsze = [i for i in range(2, 61) if all(i % j != 0 for j  in range(2, int(i**0.5)+1))]

print(pierwsze)