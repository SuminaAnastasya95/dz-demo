# Локальная область видимости
def my_func():
    x = 10
    print(x)


my_func()
# print(x)

# Глобальная область

a = 20


def show():
    print(a)


# a = 20 Так еще он найдет чему равно а
show()
# a = 20  Тут уже нет, и переменная должна быть объявлена до ее исполнения


def print(*value: str, sep: str = "-"):
    return "-".join(value)


print(print("a", "b", "c"))
