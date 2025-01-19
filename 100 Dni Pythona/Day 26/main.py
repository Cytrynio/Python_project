
lista = [1,2,[3,4],[5,6,7,[8,9,[10,11]]]]


def splaszczenie(x):
    return [item for i in x for item in (splaszczenie(i) if isinstance(i,list) else [i])]


print(splaszczenie(lista))
