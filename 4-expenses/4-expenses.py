# add_expense(expenses, value) — добавляет расход
# delete_expence(expenses, index) — удалить расход
# get_total(expenses) — возвращает сумму
# get_average(expenses) — возвращает средний расход
# print_report(expenses) — печатает красивый отчёт
# Вызывать все функции в меню. Расходы хранить в list
from typing import List


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


expenses: List[str] = ['15.00', '10.00', '100.00']
add_expense(expenses, money())
print(f"✅Список состоит из элементов - {expenses}")


def delete_expence(expenses_lists: List[str], delete_element: str):
    """удалить расход"""
    delete_element = str(
        input(f"Какой элемент удалить? Список состоит из - {expenses} "))
    if not delete_element.count("."):
        result_element = delete_element + ".00"
        index_list = expenses.index(result_element)
        expenses.pop(index_list)
    elif delete_element.count(delete_element):
        index_list = expenses.index(delete_element)
        expenses.pop(index_list)
    else:
        print("⚠️ Элемент не найден")


delete_expence(expenses, "10")
print(f"✅ После удаления список выглядит так - {expenses}")


def get_total(result_sum: List[str]) -> float:
    """Возвращает сумму"""
    total_sum = 0.0
    for fruit in result_sum:
        float_f = float(fruit)
        total_sum += float_f
    return total_sum


total_sum = get_total(expenses)
print(f"✅ Сумма все расходов - {total_sum}")


def get_average(total_sum: float, expenses_lists: List[str]) -> float:
    """возвращает средний расход"""
    return round(total_sum / len(expenses_lists), 2)


total_advg = get_average(total_sum, expenses)
print(f"✅ Среднее значение затрат - {total_advg}")


def print_report(expenses_lists: List[str], get_sum: float, get_avg: float):
    print(f"Список состоит из элементов - {expenses_lists}\n")
    print(f"После удаления список выглядит так - {expenses_lists}\n")
    print(f"Сумма все расходов - {get_sum}\n")
    print(f"Сумма все расходов - {get_avg}\n")


# report = print_report(expenses, get_sum=total_sum, get_avg=total_advg)
print("===ОТЧЕТ РАСХОДОВ===")
print_report(expenses, get_sum=total_sum, get_avg=total_advg)
print("===КОНЕЦ===")
