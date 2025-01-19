# from abc import ABC, abstractmethod
#
# class Metoda_płatności(ABC):
#
#     @abstractmethod
#     def autoryzuj(self,kwota):
#         pass
#
#     @abstractmethod
#     def wykonaj_przelew(self,kwota):
#         pass
#
#
# class Karta_Kredytowa(Metoda_płatności):
#     def autoryzuj(self,kwota):
#         print(f"Autoryzacja płatności kartą kredytową na kwotę: {kwota} PLN.")
#
#     def wykonaj_przelew(self,kwota):
#         print(f"Płatność kartą kredytową: {kwota} PLN została wykonana.")
#
# class PayPal(Metoda_płatności):
#     def autoryzuj(self,kwota):
#         print(f"Autoryzacja płatności przez PayPal na kwotę: {kwota} PLN.")
#
#     def wykonaj_przelew(self,kwota):
#         print(f"Płatność przez PayPal: {kwota} PLN została wykonana.")
#
#
# class Przelew_Bankowy(Metoda_płatności):
#
#     def autoryzuj(self,kwota):
#         print(f"Autoryzacja przelewu bankowego na kwotę: {kwota} PLN.")
#
#     def wykonaj_przelew(self,kwota):
#         print(f"Przelew bankowy: {kwota} PLN został wykonany.")
#
#
# def przetwórz_platnosc (metoda: Metoda_płatności, kwota):
#     metoda.autoryzuj(kwota)
#     metoda.wykonaj_przelew(kwota)
#
#
# karta = Karta_Kredytowa()
# paypal = PayPal()
# przelew = Przelew_Bankowy()
#
#
# przetwórz_platnosc(karta,150)
# przetwórz_platnosc(paypal,300)
# przetwórz_platnosc(przelew,300)
from random import random


#
#
# def anagramchecker(word1, word2):
#     if sorted(word1) == sorted(word2):
#         print("Anagram")
#     else:
#         print("Not anagram")
#
# anagramchecker("tell", "let")
#
#
# def palindrome():
#     text = input("Wpisz słowo")
#     text_nospace = text.replace(" ", "").lower()
#     if text_nospace == text_nospace[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
#
# palindrome()



# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if lista[j] > lista[j+1]:
#                 lista[j],lista[j+1] = lista[j+1],lista[j]
#     return lista
#
#
# x = [5,6,2,88,72,65,24]
#
# print(bubble_sort(x))
#
#
# lista = [5, 12, 8, 20, 3, 9, 17]
#
# wieksze_od_10 = [x for x in lista if x > 10]
#
# print(wieksze_od_10)
# kwadraty = [x for x in range(0,10) if x %2 == 0]
#
# print(kwadraty)

import random

marka_auta = ["VW","Skoda","Seat","Toyota","Hyundai","Ford"]
model = ["Cabrio","Suv","Sedan","Hatchback"]
marka_motoru = ["Yamaha","Honda","Kawasaki"]

class Car:
    def __init__(self):
        self.marka = random.choice(marka_auta)
        self.model = random.choice(model)
        self.rocznik = random.randint(1990,2024)
        self.pojemnosc_baku = 50
        self.przebieg = random.randint(0,200000)
        self.ilosc_paliwa = random.randint(0,50)
        self.spalanie = 6

    def dodawanie_paliwa(self,tankowanie):
        if self.ilosc_paliwa + int(tankowanie) >= self.pojemnosc_baku:
            print("Masz wystarczająco dużo paliwa")
        else:
            self.ilosc_paliwa += int(tankowanie)

    def przejechanie_dystansu(self,dystans):
        liczba_km = int(dystans)
        if liczba_km > 100:
            self.ilosc_paliwa -= self.spalanie
        else:
            self.spalanie *= 0.5
        self.przebieg += liczba_km

        print(f"Przejechałeś {liczba_km}km")

    def display(self):
        print(f"Twoje auto \nMarka: {self.marka}\nModel: {self.model} \nRocznik: {self.rocznik} \nIlość paliwa: {self.ilosc_paliwa}l\nPrzebieg: {self.przebieg}")




class Motor(Car):
    def __init__(self):
        super().__init__()
        self.marka = random.choice(marka_motoru)
        self.model = "Ścigacz"
        self.pojemnosc_baku = 25
        self.ilosc_paliwa = random.randint(0, 25)

    def display(self):
        print(
            f"Twoj motocykl \nMarka: {self.marka}\nModel: {self.model} \nRocznik: {self.rocznik} \nIlość paliwa: {self.ilosc_paliwa}l\nPrzebieg: {self.przebieg}")

car1 = Car()
car1.display()
print("\n")
car1.dodawanie_paliwa(1)
car1.display()
print("\n")
car1.przejechanie_dystansu(90)
print("\n")
car1.display()

motocykl = Motor()

motocykl.display()
motocykl.dodawanie_paliwa(25)
motocykl.display()