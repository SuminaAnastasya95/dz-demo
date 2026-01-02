# Задача 4 (по желанию): Глобальный счётчик тестов 🧪
# Создай переменную test_count = 0.
# Напиши функцию run_test(name), которая:

# увеличивает test_count на 1
# выводит: "Запущен тест №{test_count}: {name}"
# → Используй global.

test_count = 0


def run_test(name):
    global test_count
    test_count += 1
    return test_count


name = "name"
print(f'Запущен тест № {run_test(name)}: {name}')
print(f'Запущен тест № {run_test(name)}: {name}')
