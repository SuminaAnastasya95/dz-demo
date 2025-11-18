from typing import List

expenses: List[str] = []


def menu():
    while True:
        print("\nВыберите номер меню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать сумму и средний расход")
        print("4. Удалить расход по номеру")
        print("5. Отчет")
        print("0. Выход")

        user_input = input("→ ").strip()

        # Проверка: пустой ввод
        if not user_input:
            print("⚠️ Введите число.")
            continue

        # Проверка: состоит ли строка ТОЛЬКО из цифр (и, возможно, знака '-')
        if not user_input.isdigit():  # .isdigit() → True только для неотрицательных целых
            print("❌ Введите целое число от 0 до 5.")
            continue

        user_choice = int(user_input)

        if user_choice == 0:
            print("Выход из программы. До свидания!")
            break

        elif user_choice == 1:
            handle_add_expense()

        elif user_choice == 2:
            handle_show_expenses()

        elif user_choice == 3:
            handle_show_summary()

        elif user_choice == 4:
            handle_delete_expense()

        elif user_choice == 5:
            handle_report()

        else:
            print("⚠️ Неверный выбор. Введите число от 0 до 5.")


# Обработчики
def handle_add_expense():
    amount_str = money()
    if amount_str is not None:  # Успешный парсинг
        add_expense(amount_str)
        print(f"✅ Расход {amount_str} руб. добавлен.")
    else:
        print("❌ Ошибка ввода. Возврат в меню.")


def handle_show_expenses():
    if not expenses:
        print("📭 Список расходов пуст.")
    else:
        print("📌 Все расходы:")
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp} руб.")


def handle_show_summary():
    if not expenses:
        print("📭 Нет расходов.")
    else:
        # Без float-ошибок: все значения — строки вида "100.50"
        total = sum(float(x) for x in expenses)
        avg = total / len(expenses)
        print(f"💰 Всего: {total:.2f} руб. | Средний: {avg:.2f} руб.")


def handle_delete_expense():
    if not expenses:
        print("📭 Нечего удалять.")
        return

    idx_input = input(f"Введите номер расхода (1–{len(expenses)}): ").strip()
    if not idx_input.isdigit():
        print("❌ Номер должен быть целым числом.")
        return

    idx = int(idx_input) - 1
    if 0 <= idx < len(expenses):
        removed = expenses.pop(idx)
        print(f"🗑️ Удалён расход: {removed} руб.")
    else:
        print("❌ Неверный номер.")


def handle_report():
    print("📈 Отчёт: пока не реализован.")


# Функция money() — переписана БЕЗ exit() и БЕЗ исключений
def money() -> str | None:
    # None — сигнал об ошибке
    input_text = input("Введите сумму (пример: 100 руб 10 коп): ").strip()
    if not input_text:
        return None

    normal_text = " ".join(input_text.split()).lower()
    parts = normal_text.split()

    # Проверка минимальной длины
    if len(parts) < 2:
        return None

    rub_str, rub_unit = parts[0], parts[1]

    # Проверка: рубли — целое неотрицательное число
    if not rub_str.isdigit():
        return None
    if rub_unit != "руб":
        return None

    # Копейки: либо нет, либо ровно 2 слова ещё
    if len(parts) == 2:
        kopecks = "00"
    elif len(parts) == 4:
        kop_str, kop_unit = parts[2], parts[3]
        if not kop_str.isdigit():
            return None
        if kop_unit != "коп":
            return None
        # Ограничиваем двумя цифрами (на случай "123 коп" → "23")
        kopecks = kop_str.zfill(2)[-2:]
    else:
        return None

    return f"{rub_str}.{kopecks}"


def add_expense(amount: str):
    expenses.append(amount)


# Запуск
if __name__ == "__main__":
    menu()
