# Задача 1: Простое число
# Напиши функцию is_prime(n), которая возвращает True, если n — простое число, и False — иначе.

# 💡 Простое — делится только на 1 и на себя.
# Проверяй делители от 2 до int(n**0.5) + 1.

# Примеры:
# is_prime(2)  # True
# is_prime(4)  # False
# is_prime(17) # True

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(is_prime(17))
