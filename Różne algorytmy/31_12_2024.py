#
# class ToDoList:
#     def __init__(self):
#         self.tasks = []
#         self.completed_task = []
#
#     def add_task(self,task):
#         self.tasks.append(task)
#
#     def remove_task(self,task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#         else:
#             print("Nie ma takiego zadania")
#
#     def mark_as_completed(self,task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             self.completed_task.append(task)
#         else:
#             print('Nie ma takiego zadania')
#
#     def show_tasks(self):
#         if len(self.tasks) >= 0:
#             print(f"Zadania w toku: {self.tasks}")
#         else:
#             print("Lista pusta, dodaj zadanie do wykonania")
#
#
#     def show_completed_tasks(self):
#         if len(self.completed_task) >= 0:
#             print(f"Zadania zakończone: {self.completed_task}")
#         else:
#             print("Lista pusta, wykonaj zadania")
#
#     def clear_completed_tasks(self):
#         self.completed_task.clear()
#
# lista1 = ToDoList()
# lista1.add_task("Jedzenie chrupek")
# lista1.add_task("Sranie")
# lista1.add_task("Jedzenie")
# lista1.add_task("Spanie")
# lista1.show_tasks()
# lista1.remove_task("Jedzenie chrupek")
# lista1.mark_as_completed("Sranie")
# lista1.show_tasks()
# lista1.show_completed_tasks()
# lista1.clear_completed_tasks()
# lista1.show_completed_tasks()
from PIL.ImImagePlugin import number


# duplikat = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,9,9]
#
#
# def usuwanie_duplikatów(lista):
#     lista_bez_dupli = []
#     for i in lista:
#         if i not in lista_bez_dupli:
#             lista_bez_dupli.append(i)
#     return lista_bez_dupli
#
#
# sprawdzona_lista = usuwanie_duplikatów(duplikat)
#
# print(sprawdzona_lista)



def liczna_pierwsza(zakres):
    l_pierwsze = []
    for i in range(2,zakres):
        if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            l_pierwsze.append(i)
    return l_pierwsze

print(liczna_pierwsza(100))



def silnia(num):
    if num ==0:
        return 1
    else:
        return num * silnia(num-1)


print(silnia(5))