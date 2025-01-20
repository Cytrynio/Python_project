# Anagram
#
#
# def anagram(word1,word2):
#     if sorted(word1.lower()) == sorted(word2.lower()):
#         print("Anagram")
#     else:
#         print("Not anagram")
#
# anagram("silent","listen")
# anagram("Dupa","padu")
# anagram("dupski","parówka")
#
#
# def bubble_sort(x):
#     n=len(x)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if x[j] > x[j+1]:
#                 x[j],x[j+1] = x[j+1],x[j]
#     return x
#
# lista_numerów = [1,4,5,6,7,4,33,2,2,22,3,4,55,6,7,1]
#
# posortowana_lista = sorted(lista_numerów)
#
# print(bubble_sort(lista_numerów))
# print(posortowana_lista)
#
#
# # Bubblesort
#
#
#
# # Klasa student
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def avg(self):
#         avg_grades = round(sum(self.grades) / len(self.grades),2)
#         print(avg_grades)
#         return avg_grades
#     def show_grades(self):
#         print(f"{self.grades}")
#
# student1 = Student("Marcin")
# student1.add_grade(4)
# student1.add_grade(5)
# student1.add_grade(2)
# student1.add_grade(3)
# student1.add_grade(4)
# student1.add_grade(6)
# student1.add_grade(1)
# student1.show_grades()
# student1.avg()
#
#
#
# # Palindrome
#
# def palindrome(word1):
#     reversed_word = word1[::-1]
#     if word1 == reversed_word:
#         print("It's palindrome")
#     else:
#         print("Its not a palindrome")
#
# # Liczby pierwsze



def pierwsze(numer):
    if numer < 2:
        print("To nie liczba pierwsza")
    for i in range(2,int(numer**0.5)+1):
        if numer % i == 0:
            print("To nie liczba pierwsza")
    print("To liczba pierwsza")

pierwsze(6)
pierwsze(5)
# # Silnia
#
# def silnia(num):
#     if num == 0:
#         return 1
#     else:
#         return num * silnia(num-1)
#
# print(silnia(5))
#
# # Duplikaty
# def duplikaty(l):
#     lista_bez_dupli = []
#     for i in l:
#         if i not in lista_bez_dupli:
#             lista_bez_dupli.append(i)
#     return lista_bez_dupli
#
# print(duplikaty(lista_numerów))


# samogloski
def samogloski(text):
    num = 0
    vowels = "aeiou"
    new_text = text.lower()
    for i in new_text:
        if i in vowels:
            num += 1
    return num

print(samogloski("DAAAAAupa maryny ratatatatata"))



# # największa liczba bez max
# def najwieksza(l):
#     largest = l[0]
#     for i in l:
#
#         if i > largest:
#             largest = i
#     return largest
#
# print(najwieksza(lista_numerów))
#
#
#
# # liczby parzyste with list cophertazion
#
#
# parzyste = [x for x in range(1,101) if x % 2 == 0]
# print(parzyste)
# # fizzbuzz