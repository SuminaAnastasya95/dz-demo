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
delete_element = str(
    input(f"Какой элемент удалить? Список состоит из - {expenses} "))
if not delete_element.count("."):
    result_element = delete_element + ".00"
    index_list = expenses.index(result_element)
    expenses.pop(index_list)
elif delete_element.count(delete_element):  # type: ignore
    index_list = expenses.index(delete_element)
    expenses.pop(index_list)
else:
    print("Элемент не найден")
