# add_expense(expenses, value) — добавляет расход
# delete_expence(expenses, index) — удалить расход
# get_total(expenses) — возвращает сумму
# get_average(expenses) — возвращает средний расход
# print_report(expenses) — печатает красивый отчёт
# Вызывать все функции в меню. Расходы хранить в list
from typing import List


def choise_func(expenses_lists: List[str] = []):
    while True:
        print(("Выберите номер меню: \n"
               "1. Добавить расход\n"
               "2. Удалить расход по номеру\n"
               "3. Показать сумму расходов\n"
               "4. Показать среднюю сумму расходов\n"
               "5. Отчет\n"
               "0. Выход\n"))
        user_choice = input("-> ")
        int_user_choice = int(user_choice)
        if int_user_choice == 0:
            print("Выход из приложения. До свидания!")
            break
        elif int_user_choice == 1:
            add_expense(expenses_lists, money())
        elif int_user_choice == 2:
            index = str(
                input(f"Какой элемент удалить? Список состоит из - {expenses_lists} "))
            delete_expence(expenses_lists, index)
        elif int_user_choice == 3:
            f_get_total = get_total(expenses_lists)
            print(f"Сумма расходов составляет - {f_get_total:.2f} руб.")
        elif int_user_choice == 4:
            f_get_average = get_average(expenses_lists)
            print(
                f"Средняя сумма расходов составляет - {f_get_average:.2f} руб.")
        elif int_user_choice == 5:
            print_report(expenses_lists)


def money() -> str:
    input_text = input("Какую сумму вы потратили: (пример: 100 руб 10 коп) ")
    normal_text = " ".join(input_text.split()).lower()
    splits = normal_text.split(" ")

    if len(splits) < 1 or not splits[0].isnumeric():
        print("Некорректный формат суммы, отсутствует целая часть")
        exit()
    if len(splits) < 2 or splits[1] != "руб":
        print("Некорректный формат суммы, отсутствует руб")
        exit()
    if len(splits) == 2:
        return f"{splits[0]}.00"
    if len(splits) < 3 or not splits[2].isnumeric():
        print("Некорректный формат суммы, отсутствует копейки часть")
        exit()
    if len(splits) < 4 or splits[3] != "коп":
        print("Некорректный формат суммы, отсутствует коп")
        exit()

    return f"{splits[0]}.{int(splits[2]):02d}"


def add_expense(expenses_lists: List[str], total_money: str):
    """добавляет расход"""
    expenses_lists.append(total_money)


def delete_expence(expenses_lists: List[str], delete_element: str):
    """удалить расход"""
    if not expenses_lists:
        print("⚠️Список пустой, добавьте затраты через п.1")
    elif not delete_element.count("."):
        result_element = delete_element + ".00"
        index_list = expenses_lists.index(result_element)
        expenses_lists.pop(index_list)
    elif expenses_lists.count(delete_element):
        index_list = expenses_lists.index(delete_element)
        expenses_lists.pop(index_list)
    else:
        print("⚠️ Элемент не найден")


def get_total(result_sum: List[str]) -> float:
    """Возвращает сумму"""
    total_sum = 0.0
    for fruit in result_sum:
        float_f = float(fruit)
        total_sum += float_f
    return total_sum


def get_average(expenses_lists: List[str]):
    """возвращает средний расход"""
    if not expenses_lists:
        return 00.00
    else:
        total_sum = 0
        for i in expenses_lists:
            i_float = float(i)
            total_sum += i_float
        total_avg = round(total_sum / len(expenses_lists), 2)
        return total_avg


def print_report(expenses_lists: List[str]):
    total_sum = get_total(expenses_lists)
    total_avg = get_average(expenses_lists)
    print("===ОТЧЕТ РАСХОДОВ===")
    print(f"Список состоит из элементов - {expenses_lists}\n")
    print(f"После удаления список выглядит так - {expenses_lists}\n")
    print(f"Сумма все расходов - {total_sum:.2f} руб.\n")
    print(f"Сумма все расходов - {total_avg:.2f} руб.\n")
    print("===КОНЕЦ===\n")


choise_func()
