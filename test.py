# **Описание**: Создайте функцию make_multiplier, которая принимает число n и возвращает новую функцию, умножающую свой аргумент на n.
#
# **Входные данные**: Число n для создания функции-умножителя
#
# **Выходные данные**: Функция, которая умножает переданное ей число на n
#
# **Ограничения**: Используйте только базовые операции Python
#
# **Примеры**:
# Input:
# multiply_by_3 = make_multiplier(3)
# result = multiply_by_3(4)
# Output: 12
#
# Input:
# multiply_by_5 = make_multiplier(5)
# result = multiply_by_5(7)
# Output: 35

def make_multiplier(n):
    return lambda x: x*n


# Тестовые данные
print(make_multiplier(4))
test_value1 = 4

test_multiplier2 = 5
test_value2 = 7

# Вызовы для проверки
# multiply_by_3 = make_multiplier(test_multiplier1)
# result1 = multiply_by_3(test_value1)
# print(result1)  # Должно быть 12

# multiply_by_5 = make_multiplier(test_multiplier2)
# result2 = multiply_by_5(test_value2)
# print(result2)  # Должно быть 35
