# **Описание**: Создайте функцию filter_and_transform, которая принимает список чисел, функцию-фильтр и функцию-преобразователь, и возвращает новый список с элементами, прошедшими фильтр и преобразованными.
#
# **Входные данные**:
# - numbers: список чисел
# - filter_func: функция для фильтрации (возвращает True/False)
# - transform_func: функция для преобразования элементов
#
# **Выходные данные**: Список преобразованных элементов, прошедших фильтр
#
# **Ограничения**: Используйте только базовые операции Python, не используйте встроенные filter/map
#
# **Примеры**:
# Input:
# numbers = [1, 2, 3, 4, 5, 6]
# def is_even(x): return x % 2 == 0
# def square(x): return x * x
# result = filter_and_transform(numbers, is_even, square)
# Output: [4, 16, 36]
#
# Input:
# numbers = [10, 15, 20, 25, 30]
# def greater_than_15(x): return x > 15
# def double(x): return x * 2
# result = filter_and_transform(numbers, greater_than_15, double)
# Output: [40, 50, 60]

def filter_and_transform(numbers, filter_func, transform_func):

    # Ваш код здесь
return [transform_func(x) for x in numbers if filter_func(x)]


# Тестовые данные
test_numbers1 = [1, 2, 3, 4, 5, 6]
test_numbers2 = [10, 15, 20, 25, 30]


def is_even(x):
    return x % 2 == 0


def square(x):
    return x * x


def greater_than_15(x):
    return x > 15


def double(x):
    return x * 2


# Вызовы для проверки
result1 = filter_and_transform(test_numbers1, is_even, square)
print(result1)  # Должно быть [4, 16, 36]

result2 = filter_and_transform(test_numbers2, greater_than_15, double)
print(result2)  # Должно быть [40, 50, 60]
