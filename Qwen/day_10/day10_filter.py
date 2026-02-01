# Задача 2: filter() и простые числа
# Напиши функцию is_prime(n), затем используй filter(), чтобы оставить простые числа из списка:
data = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_prime(data):
    if data < 1:
        return False
    for element in range(2, int(data**0.5) + 1):
        if data % element == 0:
            return False
        return True


total_data = list(filter(is_prime, data))
print(total_data)
