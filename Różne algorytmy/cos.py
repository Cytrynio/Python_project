class Samochód:
    def __init__(self,marka,model,rocznik):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
    def opis(self):
        return f"{self.rocznik} {self.marka} {self.model}"

auto = Samochód("Toyota", "Corolla", 2020)
print(auto.opis())  # Wynik: "2020 Toyota Corolla"

