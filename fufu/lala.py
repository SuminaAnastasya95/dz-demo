from typing import List


# def delete_expence(expenses_lists: List[str], delete_element: str):
#     """удалить расход"""
#     delete_element = str(
#         input(f"Какой элемент удалить? Список состоит из - {expenses_lists} "))
#     if not delete_element.count("."):
#         result_element = delete_element + ".00"
#     if result_element.count(delete_element):  # type: ignore
#         index_list = expenses_lists.index(delete_element)
#         expenses_lists.pop(index_list)
#     else:
#         print("Элемент не найден")


# expenses: List[str] = ['15.00', '10.00', '100.00']
# delete_expence(expenses, "10")
# print(f"После удаления список выглядит так - {expenses}")


expenses: List[str] = ['15.00', '10.00', '100.00']


def get_total(result_sum: List[str]) -> float:
    """Возвращает сумму"""
    total_sum = 0.0
    for fruit in result_sum:
        float_f = float(fruit)
        total_sum += float_f
    print(f"Сумма расходов составляет: {total_sum:.2f} руб.")
    return total_sum


# total_sum = get_total(expenses)
# print(f"✅ Сумма все расходов - {total_sum}")


def get_average(expenses_lists: List[str]):
    """возвращает средний расход"""
    total_sum = get_total(expenses_lists)
    total_avg = get_average(expenses_lists)
    if not expenses_lists:
        print_avg = ("Сумма = 00.00. Т.к. список затрат пустой")
        return print_avg
    else:
        total_sum = 0
        for i in expenses_lists:
            i_float = float(i)
            total_sum += i_float
        total_avg = round(total_sum / len(expenses_lists), 2)
        print(f"Сумма среднего расхода составляет: {total_avg:.2f} руб.")
        return total_avg


# total_advg = get_average(total_sum, expenses)
# print(f"✅ Среднее значение затрат - {total_advg}")


def print_report(expenses_lists: List[str], total_sum: float, total_avg: float):
    print("===ОТЧЕТ РАСХОДОВ===")
    print(f"Список состоит из элементов - {expenses_lists}\n")
    print(f"После удаления список выглядит так - {expenses_lists}\n")
    print(f"Сумма все расходов - {total_sum}\n")
    print(f"Сумма все расходов - {total_avg}\n")
    print("===КОНЕЦ===")


print_report(expenses)
