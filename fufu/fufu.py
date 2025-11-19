# def add_numbers(a, b):  #add_numbers - название фукции, (a, b) аргументы функции
#     res = a + b
#     return res #Что возвращает функция, если этого return нет, то функция будет возвращать None


def print_hello(user_name: str):
    print(f"Привет, {user_name}!")


print_hello("Антон")
res = print_hello("Вася")
print(res)  # None
print(type(res))  # <class 'NoneType'>


def multiply(a: int, b: int) -> int:
    return a * b


res = multiply(4, 5)
print(res)
