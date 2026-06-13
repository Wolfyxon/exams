
"""
************************************************
klasa: Notatka
opis: Wirtualna notatka z tytułem i treścią
pola: __tytul - tytuł notatki
      __tresc - treść notatki
      __ilosc_notatek - (statyczne) Ilość stworzonych notatek
      __id - Identyfikator notatki generowany na podstawie ich ilości
autor: 1234567890
************************************************
"""
class Notatka:
    __ilosc_notatek = 0

    def __init__(self, tytul: str, tresc: str) -> None:
        Notatka.__ilosc_notatek += 1

        self.__id = Notatka.__ilosc_notatek
        self._tytul = tytul
        self._tresc = tresc

    def wyswietl(self) -> None:
        print(f"{self._tytul}: {self._tresc}")

    def debug(self) -> None:
        print(f"ilosc_notatek = {self.__ilosc_notatek}; id = {self.__id}; tytul = {self._tytul}; tresc = {self._tresc}")
    
def main() -> None:
    not_a = Notatka("mleko", "kupić mleko")
    not_b = Notatka("inwokacja", "Litwo! Ojczyzno moja! ty jesteś jak zdrowie")

    print("Notatka A:")
    not_a.wyswietl()
    not_a.debug()
    print()

    print("Notatka B:")
    not_b.wyswietl()
    not_b.debug()
    print()

if __name__ == "__main__":
    main()