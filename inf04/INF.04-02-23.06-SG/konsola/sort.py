import random

def bubble_sort(array) -> None:
    sorted = False
    
    while not sorted:
        sorted = True

        for i in range(len(array) - 1):
            current = array[i]
            next = array[i + 1]

            if next < current:
                array[i] = next
                array[i + 1] = current

                sorted = False

def get_random_array(length: int) -> list[int]:
    res = []

    for _ in range(length):
        res.append(random.randint(0, 1000))

    return res

def main() -> None:
    count = 100
    rand_array = get_random_array(100)
    
    bubble_sort(rand_array)

    print(f"Posortowana tablica {count} pseudolosowych liczb:")

    for v in rand_array:
        print(v, end=" ")
    
    print()

if __name__ == "__main__":
    ####### TEST ###########
    test_rand_array = get_random_array(100)
    bubble_sort(test_rand_array)

    for i in range(len(test_rand_array) - 1):
        current = test_rand_array[i]
        next = test_rand_array[i + 1]

        assert current <= next, f"Element {i} ({current}) > {i + 1} ({next}): {test_rand_array}"

    print("Test zakończony pomyślnie")
    #######################

    main()

