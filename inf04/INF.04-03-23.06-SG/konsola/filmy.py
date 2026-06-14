
"""
******************************************************
nazwa klasy: Film
pola: _tytul        - Tytuł filmu
      _wypozyczenia - Ilość wypożyczeń
metody: set_tytul,        None - Ustawia tytuł filmu
        get_tytul,        str  - Zwraca tytuł filmu
        wypozycz,         None - Inkrementuje ilość wypożyczeń
        get_wypozyczenia, int - Zwraca ilość wypożyczeń
informacje: Klasa reprezentuje filmy
autor: 1234567890
*****************************************************
"""
class Film:
    def __init__(self, tytul: str) -> None:
        self._tytul = tytul
        self._wypozyczenia = 0

    def set_tytul(self, tytul: str) -> None:
        self._tytul = tytul

    def get_tytul(self) -> str:
        return self._tytul 

    def wypozycz(self) -> None:
        self._wypozyczenia += 1

    def get_wypozyczenia(self) -> int:
        return self._wypozyczenia

def main() -> None:
    film = Film("Shrek")
    print(f"Tytuł: {film.get_tytul()} Ilość wypożyczeń: {film.get_wypozyczenia()}")

    print("Zmieniam tytuł i wypożyczam...")

    film.set_tytul("Shrek 2")
    film.wypozycz()

    print(f"Nowy tytuł: {film.get_tytul()} Ilośc wypożyczeń: {film.get_wypozyczenia()}")

if __name__ == "__main__":
    main()
