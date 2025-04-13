import pickle
import os
import random

# Klasa reprezentująca książkę
class Book:
    def __init__(self, title, author, year):
        # Walidacja: sprawdzenie, czy tytuł jest niepusty
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        # Walidacja: sprawdzenie, czy autor jest niepusty
        if not author.strip():
            raise ValueError("Autor nie może być pusty!")
        # Walidacja: sprawdzenie, czy rok jest liczbą całkowitą
        if not str(year).isdigit():
            raise ValueError("Rok musi być liczbą całkowitą!")

        # Przypisanie wartości do atrybutów obiektu
        self.title = title.strip()
        self.author = author.strip()
        self.year = int(year)

    # Funkcja do wyświetlania książki w przyjaznym formacie
    def __str__(self):
        return f"📖 {self.title} – {self.author} ({self.year})"

# Klasa reprezentująca film
class Movie:
    def __init__(self, title, director, year):
        # Walidacja: sprawdzenie, czy tytuł jest niepusty
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        # Walidacja: sprawdzenie, czy reżyser jest niepusty
        if not director.strip():
            raise ValueError("Reżyser nie może być pusty!")
        # Walidacja: sprawdzenie, czy rok jest liczbą całkowitą
        if not str(year).isdigit():
            raise ValueError("Rok musi być liczbą całkowitą!")

        # Przypisanie wartości do atrybutów obiektu
        self.title = title.strip()
        self.director = director.strip()
        self.year = int(year)

    # Funkcja do wyświetlania filmu w przyjaznym formacie
    def __str__(self):
        return f"🎬 {self.title} – reż. {self.director} ({self.year})"

# Klasa reprezentująca grę planszową
class BoardGame:
    def __init__(self, title, publisher, players):
        # Walidacja: sprawdzenie, czy tytuł jest niepusty
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        # Walidacja: sprawdzenie, czy wydawca jest niepusty
        if not publisher.strip():
            raise ValueError("Wydawca nie może być pusty!")
        # Walidacja: sprawdzenie, czy liczba graczy jest liczbą całkowitą
        if not str(players).isdigit():
            raise ValueError("Liczba graczy musi być liczbą całkowitą!")

        # Przypisanie wartości do atrybutów obiektu
        self.title = title.strip()
        self.publisher = publisher.strip()
        self.players = int(players)

    # Funkcja do wyświetlania gry planszowej
    def __str__(self):
        return f"🎲 {self.title} – {self.publisher}, dla {self.players} graczy"

# Klasa reprezentująca grę wideo
class VideoGame:
    def __init__(self, title, platform, developer):
        # Walidacja: sprawdzenie, czy tytuł jest niepusty
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        # Walidacja: sprawdzenie, czy platforma jest niepusta
        if not platform.strip():
            raise ValueError("Platforma nie może być pusta!")
        # Walidacja: sprawdzenie, czy producent jest niepusty
        if not developer.strip():
            raise ValueError("Producent nie może być pusty!")

        # Przypisanie wartości do atrybutów obiektu
        self.title = title.strip()
        self.platform = platform.strip()
        self.developer = developer.strip()

    # Funkcja do wyświetlania gry wideo
    def __str__(self):
        return f"🎮 {self.title} – {self.platform}, {self.developer}"

# Funkcja zapisująca katalog do pliku (plik binarny)
def zapisz_katalog(katalog, plik="katalog.pkl"):
    with open(plik, "wb") as f:
        pickle.dump(katalog, f)  # Zapisz obiekt katalogu do pliku

# Funkcja wczytująca katalog z pliku
def wczytaj_katalog(plik="katalog.pkl"):
    if os.path.exists(plik):  # Sprawdzamy, czy plik istnieje
        with open(plik, "rb") as f:
            return pickle.load(f)  # Wczytujemy obiekt katalogu z pliku
    return []  # Jeśli plik nie istnieje, zwróć pustą listę

# Funkcja główna – menu aplikacji
def main():
    katalog = wczytaj_katalog()  # Wczytujemy katalog (z pliku lub pusty)

    while True:
        # Wyświetlanie menu opcji
        print("\n--- KATALOG FANTASY ---")
        print("1. Dodaj książkę")
        print("2. Wyświetl katalog")
        print("3. Edytuj pozycję")
        print("4. Dodaj film")
        print("5. Dodaj grę planszową")
        print("6. Dodaj grę wideo")
        print("7. Zakończ")
        print("8. Wylosuj przygodę ✨")
        wybor = input("Wybierz opcję: ")

        # Obsługa różnych opcji menu
        if wybor == "1":
            try:
                # Dodawanie książki
                print("\n--- Dodawanie książki ---")
                title = input("Podaj tytuł: ")
                author = input("Podaj autora: ")
                year = input("Podaj rok wydania: ")
                ksiazka = Book(title, author, year)  # Tworzymy obiekt książki
                katalog.append(ksiazka)  # Dodajemy książkę do katalogu
                zapisz_katalog(katalog)  # Zapisujemy katalog do pliku
                print("✅ Książka dodana do katalogu!")
            except ValueError as e:
                print(f"❌ Błąd: {e}")

        elif wybor == "2":
            # Wyświetlanie katalogu
            print("\n--- Twój katalog ---")
            if not katalog:  # Jeśli katalog jest pusty
                print("(Brak pozycji w katalogu)")
            else:
                for i, item in enumerate(katalog, 1):
                    print(f"{i}. {item}")  # Wyświetlamy wszystkie pozycje w katalogu

        elif wybor == "3":
            # Edytowanie pozycji w katalogu
            if not katalog:
                print("\nBrak pozycji do edycji.")
            else:
                print("\n--- Edycja pozycji ---")
                for i, item in enumerate(katalog, 1):
                    print(f"{i}. {item}")  # Wyświetlamy wszystkie pozycje do edycji
                try:
                    indeks = int(input("Podaj numer pozycji do edycji: "))
                    if 1 <= indeks <= len(katalog):  # Sprawdzamy, czy indeks jest poprawny
                        stara = katalog[indeks - 1]  # Pobieramy pozycję do edycji
                        # Obsługa różnych typów obiektów w katalogu (książka, film, gra)
                        if isinstance(stara, Book):
                            title = input("Nowy tytuł: ")
                            author = input("Nowy autor: ")
                            year = input("Nowy rok wydania: ")
                            katalog[indeks - 1] = Book(title, author, year)
                        elif isinstance(stara, Movie):
                            title = input("Nowy tytuł: ")
                            director = input("Nowy reżyser: ")
                            year = input("Nowy rok wydania: ")
                            katalog[indeks - 1] = Movie(title, director, year)
                        elif isinstance(stara, BoardGame):
                            title = input("Nowy tytuł: ")
                            publisher = input("Nowy wydawca: ")
                            players = input("Nowa liczba graczy: ")
                            katalog[indeks - 1] = BoardGame(title, publisher, players)
                        elif isinstance(stara, VideoGame):
                            title = input("Nowy tytuł: ")
                            platform = input("Nowa platforma: ")
                            developer = input("Nowy producent: ")
                            katalog[indeks - 1] = VideoGame(title, platform, developer)
                        zapisz_katalog(katalog)  # Zapisujemy zaktualizowany katalog
                        print("✅ Pozycja zaktualizowana!")
                    else:
                        print("❌ Nieprawidłowy numer pozycji.")
                except ValueError as e:
                    print(f"❌ Błąd: {e}")

        # Analogiczne opcje dla dodawania filmu, gry planszowej i gry wideo

        elif wybor == "7":
            print("Do zobaczenia!")
            break  # Kończymy działanie programu

        elif wybor == "8":
            print("\n🎲 Wylosuj przygodę ✨")
            if not katalog:
                print("😢 Katalog jest pusty – dodaj coś najpierw!")
            else:
                wybor = random.choice(katalog)  # Losowanie jednej pozycji z katalogu
                print("✨ Dziś wieczór spędzisz czas z:")
                print(wybor)  # Wyświetlamy wylosowaną pozycję

        else:
            print("❗ Nieprawidłowa opcja, spróbuj ponownie.")  # Obsługa błędnego wyboru

# Uruchomienie programu
if __name__ == "__main__":
    main()
