while True:
    user_choice = input("Выберите номер меню: \n" \
    "1. Добавить расход\n" \
    "2. Показать все расходы\n" \
    "3. Показать сумму и средний расход\n" \
    "4. Удалить расход по номеру\n" \
    "5. Выход\n")
    int_user_choice = int(user_choice)
    if int_user_choice == 5:
        break