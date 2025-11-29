# Задача 4 (по желанию): Генератор тестовых данных 🧪
# Напиши функцию generate_users(n), которая возвращает список из n словарей:
# [
#     {"id": 1, "name": "user_1"},
#     {"id": 2, "name": "user_2"},
#     ...
# ]
#  Используй цикл или list comprehension.

def generate_users(n):
    lists = []
    if n == 0:
        print("Тестовые данные не сгененировались")
    elif n >= 1:
        for n in lists:
            for_test = {"id": n, "name": f"user_{n}"}
            lists.append(for_test)
    return lists


# print(generate_users(2))


shopping_list = ["молоко", "хлеб", "яйца"]
print(shopping_list[1])
appendl = shopping_list.append("бананы")
print(appendl)
