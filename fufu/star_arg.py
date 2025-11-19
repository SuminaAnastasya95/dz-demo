def avg(*args: int):  # Для передачи неограниченного кол-ва аргументов в функции нужно использовать *
    print(type(args))
    return sum(args) / len(args)


print(avg(1, 2, 3))
print(avg(34, 100, 13, 10, 60, 90))


def print_data(name: str, *data: str):
    print(name, data)


print(print_data("Name", "a", "b", "d"))
