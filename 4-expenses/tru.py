from typing import List


# def total_pay(rub: str, cent: str):
#     total_list: List[str] = []
#     total_list.append(rub)
#     total_list.append(cent)
#     res = ','.join(total_list)
#     return res


# print(total_pay('1', '5'))


# # print(total_pay())
# a = [10, 1]
# b = ['1']
# print(','.join(a))

def choise_func():
    while True:
        user_choice = int(input("Выберите номер меню: \n"
                                "1. Добавить расход\n"
                                "2. Показать все расходы\n"
                                "3. Показать сумму и средний расход\n"
                                "4. Удалить расход по номеру\n"
                                "5. Отчет\n"
                                "0. Выход\n"))
        int_user_choice = int(user_choice)
        if int_user_choice == 0:
            break
        return user_choice


def money() -> str:
    input_text = input("Введите сумму: (пример: 100 руб 10 коп) ")
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


total = money()
expenses: List[str] = ['15', '10', '100']
add_expense(expenses, total)
print(expenses)


def delete_expence(expenses_lists: List[str], delete_element: str):
    """удалить расход"""
    delete_element = str(input(f"Какой элемент удалить? "))
    if expenses_lists.count(delete_element):
        index_list = expenses_lists.index(delete_element)
        expenses_lists.pop(index_list)
    else:
        print("Элемент не найден")


delete_expence(expenses, "10")
print(expenses)


def get_total(result_sum: List[str]) -> float:
    """Возвращает сумму"""
    total_sum = 0.0
    for fruit in result_sum:
        float_f = float(fruit)
        total_sum += float_f
    return total_sum


total_sum = get_total(expenses)
print(total_sum)


def get_average(total_sum: float, expenses_lists: List[str]) -> float:
    """возвращает средний расход"""
    return round(total_sum / len(expenses_lists), 2)


print(get_average(total_sum, expenses))
