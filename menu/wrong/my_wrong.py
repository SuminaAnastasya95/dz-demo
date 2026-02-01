class InvalidAgeError(Exception):
    pass


def set_age(age: int):
    if age < 0:
        raise InvalidAgeError("Возраст должен быть больше 0")
    return age


try:
    set_age(-1)
except InvalidAgeError as e:
    print(e)

# Можно передать несколько ошибок в except
try:
    1/0
except (ArithmeticError, ZeroDivisionError):
    print("Ошибка")


# Возможно наследование ошибок в классах
class BankError(Exception):
    pass


class ZeroFundError(BankError):
    pass
