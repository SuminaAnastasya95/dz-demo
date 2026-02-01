# 🔹 Уровень 1: Основы — создание, чтение, изменение
# Задание 1. Профиль пользователя
# Создай словарь user с ключами: "name", "age", "city".

# Выведи возраст.
# Добавь ключ "email".
# Измени город.
# Попробуй получить "phone" через .get() с дефолтом "не указан".
# 🎯 Цель: dict, [], .get(), изменение.


# user = {"name": "Nastya", "age": 30, "city": "Vidnoe"}
# print(user["age"])
# user["email"] = "email@email.com"
# print(user)
# user["city"] = "Moscow"
# print(user)
# print(user.get("phone", "не указан"))
# ----------------------------------------------------------------------

# Задание 2. Оценки по предметам
# Дан словарь:

# grades = {"math": 5, "physics": 4, "chemistry": 5}

# # Выведи все предметы (ключи).
# # Выведи все оценки (значения).
# # Выведи пары "предмет: оценка" в формате "math: 5".
# # Вычисли среднюю оценку.
# # 🎯 Цель: .keys(), .values(), .items(), sum() / len().

# print(grades.keys())
# print(grades.values())
# for subject, grade in grades.items():
#     print(f"{subject}: {grade}")
# subject = list(grades.keys())
# avg = sum(grades.values())/len(subject)
# print(f"{avg:.2f}")


# ----------------------------------------------------------------------


# Задание 3. Безопасное обновление
# Напиши функцию update_grade(grades, subject, new_grade), которая:

# Если предмет есть — обновляет оценку.
# Если нет — добавляет его.
# Возвращает обновлённый словарь.
# update_grade({"math": 5}, "physics", 4)  # → {"math": 5, "physics": 4}
# 🎯 Цель: условная логика + изменение словаря.

# grades = {"math": 5, "physics": 4, "chemistry": 5}


# def update_grade(grades: dict, subject: str, grade: int) -> dict:
#     if subject in grades:
#         grades[subject] = grade
#     else:
#         grades[subject] = grade
#     return grades


# print(update_grade({"math": 5}, "physics", 4))


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# 🔹 Уровень 2: Работа с вложенными структурами
# Задание 4. Студент с курсами
# Дан словарь:

# student = {
#     "name": "Анна",
#     "courses": {
#         "math": {"grade": 5, "credits": 4},
#         "history": {"grade": 3, "credits": 3}
#     }
# }

# # Выведи название курса "math" и его оценку.
# # Добавь курс "biology" с {"grade": 4, "credits": 2}.
# # Посчитай общий балл: сумма grade * credits / сумма credits.
# # 🎯 Цель: вложенные словари, доступ по цепочке.

# # print("Курс: ", "math")
# # print("Оценка по  math", student["courses"]["math"]["grade"])
# grade = student.get("courses", {}).get("math", {}).get("grade")
# print("Оценка по  math", grade)

# total_points = 0
# total_credits = 0
# student["courses"]["biology"] = {"grade": 4, "credits": 2}
# for course_data in student["courses"].values():
#     grades = course_data["grade"]
#     credit = course_data["credits"]
#     total_points += grades*credit
#     total_credits += credit
# gpa = total_points/total_points
# print(f"Взвешенный средний балл: {gpa:.2f}")


# proints = sum(data["grade"] * data["credits"]
#               for data in student["courses"].values())
# credit = sum(data["credits"] for data in student["courses"].values())
# gpa_v1 = proints / credit
# print(f"GPA: {gpa_v1:.2f}")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Задание 5. Поиск по вложенному словарю
students = {
    "id_001": {"name": "Оля", "age": 20},
    "id_002": {"name": "Коля", "age": 22},
    "id_003": {"name": "Маша", "age": 19}
}

# Напиши функцию find_by_name(name), которая возвращает ID студента с этим именем (первого, если несколько), или None.

# 🎯 Цель: итерация по .items(), поиск.
# name = "Оля"


# def find_by_name(students: dict, name: str):
#     for id, student in students.items():
#         if student["name"] == name:
#             return id
#         else:
#             return None


# print(find_by_name(students, "Настя"))


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# Задание 6. Обратный словарь
# Напиши функцию invert_dict(d), которая меняет ключи и значения местами.

# Пример:
invert_dict_value = {"a": 1,
                     "b": 2,
                     "c": 1}  # → {1: ["a", "c"], 2: ["b"]}

# ⚠️ Если значения повторяются — собирай ключи в список.

# 🎯 Цель: работа с дубликатами, проверка наличия ключа, if key in d.


# def invert_dict(invert: dict):
#     invert_result = {}
#     for key, value in invert.items():
#         if not value in invert_result:
#             invert_result[value] = [key]
#         elif value in invert_result:
#             invert_result[value].append(key)
#     return invert_result

# print(invert_dict(invert_dict_value))


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# Уровень 3: Преобразования и агрегации
# Задание 7. Частотный словарь
# Напиши функцию char_freq(text), которая возвращает словарь частот букв (только буквы, без учёта регистра).

# Пример:
char_freq_value = "Hello"  # → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# 🎯 Цель: str.lower(), .isalpha(), накопление в dict.


# def char_freq(text: str) -> dict:
#     lists = list(text.lower())
#     sum_element = {}
#     for element in lists:
#         if not element in sum_element:
#             sum_element[element] = 1
#         else:
#             sum_element[element] += 1
#     return sum_element


# print(char_freq(char_freq_value))


# l = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# l["e"] += 3
# print(l)


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# Задание 8. Группировка по ключу
# Дан список словарей:

orders = [
    {"item": "apple", "qty": 2, "price": 10},
    {"item": "banana", "qty": 3, "price": 5},
    {"item": "apple", "qty": 1, "price": 10}
]

# Напиши функцию group_by_item(orders), которая возвращает:
# {
#     "apple": {"total_qty": 3, "total_cost": 30},
#     "banana": {"total_qty": 3, "total_cost": 15}
# }


def group_by_item(orders: list) -> dict:
    sum_order = {}
    # total_qty_res = 0
    # total_cost_res = 0
    for order in orders:
        if not order["item"] in sum_order:
            sum_order[order["item"]] = {
                "total_qty": order["qty"], "total_cost": order["price"]}
        else:
            total_qty_res = sum(sum_order["total_qty"] + order["qty"])
            print(total_qty_res)
            total_cost_res = sum_order["total_cost"] + order["price"]
            print(total_cost_res)
            sum_order[order["item"]] = {
                "total_qty": total_qty_res, "total_cost": total_cost_res}
    return sum_order


# print(group_by_item(orders))
