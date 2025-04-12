import random

class Book:
    def __init__(self, title, author, year):
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        if not author.strip():
            raise ValueError("Autor nie może być pusty!")
        if not str(year).isdigit():
            raise ValueError("Rok musi być liczbą całkowitą!")

        self.title = title.strip()
        self.author = author.strip()
        self.year = int(year)

    def __str__(self):
        return f"📖 {self.title} – {self.author} ({self.year})"


class Movie:
    def __init__(self, title, director, year):
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        if not director.strip():
            raise ValueError("Reżyser nie może być pusty!")
        if not str(year).isdigit():
            raise ValueError("Rok musi być liczbą całkowitą!")

        self.title = title.strip()
        self.director = director.strip()
        self.year = int(year)

    def __str__(self):
        return f"🎬 {self.title} – reż. {self.director} ({self.year})"


class BoardGame:
    def __init__(self, title, publisher, players):
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        if not publisher.strip():
            raise ValueError("Wydawca nie może być pusty!")
        if not str(players).isdigit():
            raise ValueError("Liczba graczy musi być liczbą całkowitą!")

        self.title = title.strip()
        self.publisher = publisher.strip()
        self.players = int(players)

    def __str__(self):
        return f"🎲 {self.title} – {self.publisher}, dla {self.players} graczy"


class VideoGame:
    def __init__(self, title, platform, developer):
        if not title.strip():
            raise ValueError("Tytuł nie może być pusty!")
        if not platform.strip():
            raise ValueError("Platforma nie może być pusta!")
        if not developer.strip():
            raise ValueError("Producent nie może być pusty!")

        self.title = title.strip()
        self.platform = platform.strip()
        self.developer = developer.strip()

    def __str__(self):
        return f"🎮 {self.title} – {self.platform}, {self.developer}"


def main():
    katalog = []

    while True:
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

        if wybor == "1":
            try:
                print("\n--- Dodawanie książki ---")
                title = input("Podaj tytuł: ")
                author = input("Podaj autora: ")
                year = input("Podaj rok wydania: ")
                ksiazka = Book(title, author, year)
                katalog.append(ksiazka)
                print("✅ Książka dodana do katalogu!")
            except ValueError as e:
                print(f"❌ Błąd: {e}")

        elif wybor == "2":
            print("\n--- Twój katalog ---")
            if not katalog:
                print("(Brak pozycji w katalogu)")
            else:
                for i, item in enumerate(katalog, 1):
                    print(f"{i}. {item}")

        elif wybor == "3":
            if not katalog:
                print("\nBrak pozycji do edycji.")
            else:
                print("\n--- Edycja pozycji ---")
                for i, item in enumerate(katalog, 1):
                    print(f"{i}. {item}")
                try:
                    indeks = int(input("Podaj numer pozycji do edycji: "))
                    if 1 <= indeks <= len(katalog):
                        stara = katalog[indeks - 1]
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
                        print("✅ Pozycja zaktualizowana!")
                    else:
                        print("❌ Nieprawidłowy numer pozycji.")
                except ValueError as e:
                    print(f"❌ Błąd: {e}")

        elif wybor == "4":
            try:
                print("\n--- Dodawanie filmu ---")
                title = input("Podaj tytuł: ")
                director = input("Podaj reżysera: ")
                year = input("Podaj rok wydania: ")
                film = Movie(title, director, year)
                katalog.append(film)
                print("✅ Film dodany do katalogu!")
            except ValueError as e:
                print(f"❌ Błąd: {e}")

        elif wybor == "5":
            try:
                print("\n--- Dodawanie gry planszowej ---")
                title = input("Podaj tytuł: ")
                publisher = input("Podaj wydawcę: ")
                players = input("Podaj liczbę graczy: ")
                gra = BoardGame(title, publisher, players)
                katalog.append(gra)
                print("✅ Gra planszowa dodana do katalogu!")
            except ValueError as e:
                print(f"❌ Błąd: {e}")

        elif wybor == "6":
            try:
                print("\n--- Dodawanie gry wideo ---")
                title = input("Podaj tytuł: ")
                platform = input("Podaj platformę: ")
                developer = input("Podaj producenta: ")
                gra = VideoGame(title, platform, developer)
                katalog.append(gra)
                print("✅ Gra wideo dodana do katalogu!")
            except ValueError as e:
                print(f"❌ Błąd: {e}")

        elif wybor == "7":
            print("Do zobaczenia!")
            break

        elif wybor == "8":
            print("\n🎲 Wylosuj przygodę ✨")
            if not katalog:
                print("😢 Katalog jest pusty – dodaj coś najpierw!")
            else:
                wybor = random.choice(katalog)
                print("✨ Dziś wieczór spędzisz czas z:")
                print(wybor)


        else:
            print("❗ Nieprawidłowa opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()