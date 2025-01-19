import time

def stoper():
    print("Naciśnij Enter, aby rozpocząć stoper, a ponownie Enter, aby go zatrzymać.")
    input()  # Czeka na wciśnięcie Enter, aby rozpocząć
    start_time = time.time()  # Zapisuje aktualny czas jako czas startu
    print("Stoper uruchomiony!")
    
    input()  # Czeka na ponowne wciśnięcie Enter, aby zatrzymać
    end_time = time.time()  # Zapisuje aktualny czas jako czas zatrzymania
    
    elapsed_time = end_time - start_time  # Oblicza różnicę czasów
    print(f"Stoper zatrzymany! Minęło {elapsed_time:.2f} sekund.")
