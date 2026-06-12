import random

class Table:
    def __init__(self, length: int) -> None:
        value = []

        for i in range(length):
            value.append(random.randint(1, 1000))

        self.__value = value
        self.__length = length

    """
    ***********************************************
    nazwa metody: print_values
    opis metody: Wyświetla wartości tablicy i ich indeksy
    parametry: brak
    zwracany typ i opis: brak
    autor: 1234567890
    ***********************************************
    """
    def print_values(self) -> None:
        for i in range(self.__length):
            print(f"{i}: {self.__value[i]}")

    """
    ***********************************************
    nazwa metody: print_uneven
    opis metody: Wyświetla nieparzyste liczby tablicy 
                 i zwraca ich ilość
    parametry: brak
    zwracany typ i opis: int - ilość nieparzystych liczb
    autor: 1234567890
    ***********************************************
    """
    def print_uneven(self) -> int:
        res = 0

        for v in self.__value:
            if v % 2 != 0:
                print(v)
                res += 1

        return res

    """
    ***********************************************
    nazwa metody: index_of
    opis metody: Szuka podanej wartości w tablicy
    parametry: value - szukana wartość
    zwracany typ i opis: int - Indeks szukanej wartości.
                               -1 gdy nie istnieje.
    autor: 1234567890
    ***********************************************
    """
    def index_of(self, value: int) -> None:
        for i in range(self.__length):
            if self.__value[i] == value:
                return i
        
        return -1
    
    """
    ***********************************************
    nazwa metody: avg
    opis metody: Liczy średnią arytmetyczną wartości tablicy
    parametry: brak
    zwracany typ i opis: float - średnia
    autor: 1234567890
    ***********************************************
    """
    def avg(self) -> float:
        sum = 0

        for v in self.__value:
            sum += v

        return sum / self.__length

"""
***********************************************
nazwa metody: main
opis metody: Program główny
parametry: brak
zwracany typ i opis: brak
autor: 1234567890
***********************************************
"""
def main():
    tab = Table(32)

    print("Wartości tablicy:")
    tab.print_values()

    print("Liczby nieparzyste:")
    uneven = tab.print_uneven()

    print(f"Razem nieparzystych: {uneven}")

    search_num = 256
    search_idx = tab.index_of(search_num)

    if search_idx != -1:
        print(f"Znaleziono szukaną liczbę {search_num} na indeksie: {search_idx}")

    print(f"Średnia wszystkich elementów {tab.avg()}")

if __name__ == "__main__":
    main()
