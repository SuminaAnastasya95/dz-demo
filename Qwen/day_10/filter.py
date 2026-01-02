numbers = [1, 2, 3, 4, 5, 6]

# Только чётные
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # → [2, 4, 6]
