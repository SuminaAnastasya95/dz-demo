def exp(num: float, e: float = 2, mul: float = 1) -> float:
    # e: float = 2 такое равно обознаечает, что если второе число отсутствует, то п умолчанию он будет возводиться в квадрат
    return mul * num ** e


def print_data(name: str, *data: str, sep: str):
    print(name, data, sep)


print(exp(2, 3))
print(exp(e=3, num=2))
print(exp(2, mul=3))
print(exp(2))

# print_data("Vasia",  "d", "a") При такой записи будет ошибка, потому что у нас *data это неграниченное число даных, а у аргумента sep нет значения по умолчанию
print_data("Vasia",  "d", sep="a")
