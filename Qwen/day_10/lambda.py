# ambda — это анонимная (безымянная) функция, ограниченная одним выражением.
#  lambda аргументы: выражение


# Числа: Используя map и lambda, получите список квадратов чётных чисел из [1, 2, 3, 4, 5, 6].

numbers = [1, 2, 3, 4, 5, 6]
kv_nums = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0,  numbers)))
print(kv_nums)

# Строки: Есть список [' Hello ', 'WORLD', ' pyThon '].
# Приведите все строки к нижнему регистру, уберите пробелы по краям — одним map + lambda.

lists_word = [' Hello ', 'WORLD', ' pyThon ']
new_list = list(map(lambda x: x.lower().strip(), lists_word))
print(new_list)

# Кортежи: Дан список кортежей: [(1, 'a'), (2, 'b'), (3, 'c')].
# Получите список вторых элементов (['a', 'b', 'c']) через map.

list_tg = [(1, 'a'), (2, 'b'), (3, 'c')]

two_el = list(map(lambda x: x[1], list_tg))
print(two_el)


# 🟡 Уровень 2 — Фильтрация и сортировка
# Словари:
# Есть список студентов:
students = [
    {'name': 'Аня', 'grade': 'B', 'score': 85},
    {'name': 'Боря', 'grade': 'A', 'score': 92},
    {'name': 'Вася', 'grade': 'C', 'score': 70}
]

# Получите список имён студентов со score > 80.
# Отсортируйте по оценке (grade) по алфавиту ('A' → 'C').

select_student = list(map(lambda x: x['name'],
                          sorted(filter(lambda x: x['score'] > 80, students), key=lambda x: x["grade"])))

print(select_student)


# Смешанные данные:
# Есть список: [42, 'hello', [1, 2], {'x': 5}, 3.14, None].
# Напишите lambda, которая возвращает True, если элемент — число (int или float).
# Используйте с filter, чтобы оставить только числа.

random_list = [42, 'hello', [1, 2], {'x': 5}, 3.14, None]
is_only_nums = list(filter(lambda x: isinstance(
    x, (int, float)) is not isinstance(x, bool), random_list))
print(list(is_only_nums))


# Уровень 3 — Продвинутое (ближе к автотестам)
# Работа с API-подобными данными:
# Допустим, у тебя ответ от API:

products = [
    {"id": 1, "name": "Laptop", "price": 1200, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 25, "in_stock": False},
    {"id": 3, "name": "Keyboard", "price": 75, "in_stock": True}
]

# Получи список имён товаров в наличии (in_stock == True).

# Посчитай общую стоимость всех товаров в наличии — через sum(map(...)).

filter_product = list(map(lambda x: x, filter(
    lambda x: x["in_stock"] == True, products)))
print(f"Список товаров в наличи: {filter_product}")

# Найди самый дешёвый товар в наличии (используй min(..., key=lambda ...)).
min_price = min(
    filter(lambda x: x["in_stock"] == True, products), key=lambda x: x["price"])
print(f"Самый дешевый товар в наличии: {min_price}")

# Посчитай общую стоимость всех товаров в наличии — через sum(map(...)).
sum_product = sum(map(lambda x: x["price"], filter(
    lambda x: x["in_stock"] == True, products)))
print(f"Сумма всех товаров: {sum_product}")


# Валидация данных (как в автотестах):
# Создай lambda, проверяющую, что:
# строка не пустая,
# длина ≥ 3,
# содержит только буквы (.isalpha()).
# Примени её к списку: ['', 'hi', 'Anna', '3K', 'Python'] через filter.

simple_list = ['', 'hi', 'Anna', '3K', 'Python']

filter_list = list(
    filter(lambda x: isinstance(x, str) and len(x) >= 3 and x != "" and x.isalpha(), simple_list))
print(filter_list)


# Композиция проверок (полезно для assert в тестах):
# Напиши функцию all_pass(value, *predicates), принимающую значение и любое число lambda-предикатов, и возвращающую True, если все возвращают True.
# Пример:


def all_pass(value, *predicates):
    for pre in predicates:
        if not pre(value):
            return False
        return True


is_valid = all_pass(
    'Anna',
    lambda s: len(s) > 2,
    lambda s: s.isalpha(),
    lambda s: s[0].isupper()
)  # → True
print(is_valid)
