
while True:
    options = input("=== Калькулятор ===\n"
                    "1. Сложение\n"
                    "2. Вычитание\n"
                    "3. Умножение\n"
                    "4. Деление\n"
                    "0. Выход\n"
                    "Что будет считать?"
                    )
    if options.isdigit():
        print("Это не число")
        continue
    options = int(options)
    if options == 0:
        print("До свидания!")
        break
    elif options not in (1, 2, 3, 4, 0):
        print("Неверный выбор. Введите 0, 1, 2, 3 или 4.")
        continue
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))
    if options == 1:
        print(f"{number_1} + {number_2} = {number_1 + number_2}")
        continue
    if options == 2:
        print(f"{number_1} - {number_2} = {number_1 - number_2}")
        continue
    if options == 3:
        print(f"{number_1} * {number_2} = {number_1 * number_2}")
        continue
    if options == 4:
        if number_2 == 0:
            print(f"Делить на {number_2} нельзя")
        else:
            print(f"{number_1} / {number_2} = {number_1 / number_2}")
