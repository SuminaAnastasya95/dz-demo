# Задача 3: Безопасное деление
# Напиши функцию safe_divide(a, b), которая:

# возвращает a / b, если b != 0
# возвращает None, если b == 0
# Пример:
# safe_divide(10, 2)  # 5.0
# safe_divide(10, 0)  # None

def safe_divide(a, b):
    if b != 0:
        return a, b
    elif b == 0:
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))
