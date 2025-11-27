# Написать функцию calculete, которая принимает 2 числа и операцию
# "+", "-", "/", "*"

from typing import Literal


def calculate(number_1: float, number_2: float, options: Literal["+", "-", "/", "*"]):
    """Функция для расчета математических действий
    для типизации кода, мы сказали, что эта строка может принимать только определенные значения"""
    print(type(options))
    match options:
        case "+":
            return number_1 + number_2
        case "-":
            return number_1 - number_2
        case "*":
            return number_1 * number_2
        case "/":
            return number_1 / number_2 if number_2 != 0 else "Ошибка деление на 0"
        case _:
            return "Неизвестная операция"


print(calculate(10, 4, "/"))
# print(calculate(10, 0, "1"))

