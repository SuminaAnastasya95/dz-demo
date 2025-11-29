# Задача 4 (по желанию): Фильтр тест-кейсов 🧪
# Представь, что у тебя список тестов:

# python

tests = [
    {"name": "login_valid", "status": "passed"},
    {"name": "login_invalid", "status": "failed"},
    {"name": "logout", "status": "passed"},
    {"name": "profile_edit", "status": "skipped"},
]
faild_name = []
# Напиши код, который:

# создаёт список имён только упавших тестов (status == "failed")
# выводит их
# 💡 Используй цикл или list comprehension.
for test in tests:
    if test["status"] == "failed":
        faild_name.append(test["name"])
print(f"Упавший тест - {faild_name}")
