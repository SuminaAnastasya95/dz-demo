def devide(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError({"error": 1})
    return a / b


def calculate():
    try:
        devide(10, 0)
    except ZeroDivisionError as e:
        print('Деление на ноль')
        print(e)
        raise  # Можем пробросить выше, чтобы обработать ошибку в другом месте


try:
    calculate()
except ZeroDivisionError:
    print("Поймали выше")
