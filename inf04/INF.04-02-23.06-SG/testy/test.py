test_rand_array = get_random_array(100)
bubble_sort(test_rand_array)

for i in range(len(test_rand_array) - 1):
  current = test_rand_array[i]
  next = test_rand_array[i + 1]

  assert current <= next, f"Element {i} ({current}) > {i + 1} ({next}): {test_rand_array}"

print("Test zakończony pomyślnie")
