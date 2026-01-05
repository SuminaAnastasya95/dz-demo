# Задание 4. Фильтр чётных чисел 🎯
# Дан список:
numbers = [1, 4, 2, 7, 8, 3, 10]
# Создай новый список, содержащий только чётные числа.

# 💡 Подсказка: цикл + if x % 2 == 0
lists = []
for i in numbers:
    if i % 2 == 0:
        lists.append(i)
print(lists)


# Задание 5. Средний балл по классу 🎓
# Дан список студентов (список словарей):

students = [
    {"name": "Анна", "grade": 4},
    {"name": "Борис", "grade": 5},
    {"name": "Вера", "grade": 3}
]

res = 0

# Посчитай средний балл по классу.

# 💡 Цикл → сумма оценок → сумма / количество

for n in students:
    res += n["grade"]
    lens = len(students)
print(res / lens)


# 🔹 Задание 6. Общие теги тестов
# Даны множества:

smoke_tests = {"login", "logout", "main_page"}
auth_tests = {"login", "password_reset", "2fa"}

# Найди:

# общие теги (пересечение),
# все теги (объединение),
# теги только в smoke_tests (разность).

print(smoke_tests & auth_tests)
print(smoke_tests | auth_tests)
print(smoke_tests - auth_tests)
