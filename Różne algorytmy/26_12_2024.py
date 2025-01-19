
class BankAccount:
    def __init__(self,owner,numer_konta):
        self.numer_konta = numer_konta
        self.__saldo = 0
        self.owner = owner

    def deposit(self,amount):
        if int(amount) < 0:
            print("Nie możes odjąć od salda, tylko wpłać")
        else:
            self.__saldo += amount

    def withdraw(self,amount):
        if self.__saldo < amount:
            print("Nie masz wystarczająco dużo gotówki")
        else:
            self.__saldo -= amount
    def display_balance(self):
        print(f"Balance:{self.__saldo}")



wlascicel1 =  BankAccount("Marcin", 1)

wlascicel1.saldo = 200000
wlascicel1.display_balance()


# numerki = input("Daj 5 liczb")
#
# liczby = [int(liczba) for liczba in numerki.split()]
#
# wynik = [liczba**2 for liczba in liczby if liczba % 2 == 0]
#
# print(wynik)