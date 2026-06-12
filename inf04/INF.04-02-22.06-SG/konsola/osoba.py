
class Osoba:
    ilosc_osob = 0

    def __init__(self, id = 0, imie = "") -> None:
        self.__id = id
        self.__imie = imie

        Osoba.ilosc_osob += 1

    def kopiuj(self, osoba) -> None:        
        self.__id = osoba.__id
        self.__imie = osoba.__imie
    
    def __get_imie(self) -> str:
        if self.__imie == "":
            return "Brak danych"
        
        return self.__imie

    def przywitaj(self, imie) -> None:
        print(f"Cześć {imie}, mam na imię {self.__get_imie()}")


def main():
    print(f"Liczba zarejestrowanych osób to {Osoba.ilosc_osob}")

    osoba_pusta = Osoba()
    osoba_dane = Osoba(123, "Włodzimierz")

    osoba_user = Osoba(
        int(input("Podaj ID nowej osoby: ")),
        input("Podaj imię: ")
    )

    osoba_copy = Osoba()
    osoba_copy.kopiuj(osoba_user)

    osoba_pusta.przywitaj("Jan")
    osoba_dane.przywitaj("Jan")
    osoba_user.przywitaj("Jan")
    osoba_copy.przywitaj("Jan")
    
    print(f"Liczba zarejestrowanych osób to {Osoba.ilosc_osob}")

    pass

if __name__ == "__main__":
    main()