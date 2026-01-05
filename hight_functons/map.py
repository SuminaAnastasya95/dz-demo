num = [1, 2, 3, 4, 5]
# res = []
# for n in num:
#     res.append(n**2)
# print(res)


# def square(x: float):
#     return x ** 2
squares_iterator = map(lambda x: x**2, num)

squares = list(map(lambda x: x**2, num))
print(squares)


# for el in squares_iterator:
#     print(el)


a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)
