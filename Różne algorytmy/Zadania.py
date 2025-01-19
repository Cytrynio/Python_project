# # Palindrome
# def check_palindrome(text):
#     if text == text[::-1]:
#         print("To palindrone")
#     else:
#         print("To nie palindrome ")
#
# check_palindrome("213")
#
#
#
#
# # Sortowanie bubble
# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if lista[j] > lista[j + 1]:
#                 lista[j],lista[j + 1] = lista[j + 1],lista[j]
#     return lista
#
# list = [1,4,5,7,9,33,452,2,11,5,3]
#
# print(bubble_sort(list))
#
# # FizzBuzz
#
# def FizzBuzz():
#     for num in range(1,101):
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")
#         else:
#             print(num)
# print(FizzBuzz())
from itertools import count


# Liczba pierwsza
# def first(num):
#     if num == 2:
#         print("To liczba pierwsza")
#     elif num % 2 == 0 or num % 3 == 0:
#         print("Liczba nie jest pierwsza")
#     else:
#         print("To liczba pierwsza")
#
# first(4)



# vowels

# def samogloski(text):
#     num = 0
#     vowels = "aeiouAEIOU"
#     for char in text:
#         if char in vowels:
#             num += 1
#     return num
#
# print(samogloski(""))

# Duplikaty

# def dupli(lista):
#     new_list = []
#     for i in lista:
#         if i in new_list:
#             pass
#         else:
#             new_list.append(i)
#     return new_list
#
#
# listaznaków = [1,2,2,3,4,1,2,4,3,22,2,2,2]
#
# print(dupli(listaznaków))





# Symulacja systemu bankowego
# Utwórz klasę BankAccount, która pozwala na wpłaty, wypłaty i sprawdzanie salda.

# Studenci i average

# class Student():
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def average(self):
#         return round(sum(self.grades) / len(self.grades))
#
# student1 = Student("Marcin")
# 
# def test_adding_grade():
#     student1.add_grade(5)
#     assert student1.grades == [5]
# def test_average_score():
#     student1.add_grade(5)
#     student1.add_grade(6)
#     student1.add_grade(3)
#
#     assert student1.average() == 5

# a4,b5,c4,d1

# def conversion(inputed):
#     output= ""
#     for item in inputed.split(","):
#         letter = item[0]
#         count = int(item[1:])
#         output+= letter*count
#     return output
#
#
# print(conversion("a4,b5,c4,d1,e13"))
