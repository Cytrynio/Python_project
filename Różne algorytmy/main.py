
x = 12
y = 2

try:
    lista = [1]
    print(lista[0])
    print(x/y)
    print(x+4)
    print(f"Twót wynik to")
except (ZeroDivisionError, TypeError):
    print("Wystąpił jeden z dwóch błędów")
except:
    print("Inny błąd")
finally:
    print("Wykonuje się zawsze")

print("Dalsze instrukcje ...")