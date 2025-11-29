# Анонимные функции

# lambda аргумент: выражение - длина выражения не должна привышать длину строки


def square(x: float):
    return x*x


# square_lambd = lambda x: x * x такая запись после созранение страновится автоматом следующией строкой
def square_lambd(x): return x*x


# Когда полезно использовать lambda функцию?
def apply(func, value):
    return func(value)


print(apply(lambda x: x + 100, 5))
# 105
# у apply 2 аргумента. lambda x: x + 100 - это функция (func), а 5 это значение (value)

print(apply(lambda s: s.upper(), "hi"))
# HI
