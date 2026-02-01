# Задача 3: zip() и студенты
# Даны два списка:
names = ["Анна", "Борис"]
grades = [4, 5]

# Создай список словарей:
# [{"name": "Анна", "grade": 4}, {"name": "Борис", "grade": 5}]
# с помощью zip() и цикла.

pairs = zip(names, grades)
# dict_user = []
students = [{"name": name, "grade": grade}
            for name, grade in zip(names, grades)]
# for element in pairs:  # Перебираю элементы по списку
#     dict_user.append({"name": element[0], "grade": element[1]})
print(students)
