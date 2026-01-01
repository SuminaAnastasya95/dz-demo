from functools import reduce


num = [1, 2, 3, 4, 5]

print(sum(num))

res = 0
for n in num:
    res += n
print(res)

total = reduce(lambda a, b: a+b, num)
print(total)


word = ["Hi", "how", "are", "you"]
sentence = reduce(lambda a, b: a + " " + b, word)
print(sentence)


# Что такое a и b в функции reduce
def sum_custom(acc: int, next_el: int):
    return acc + next_el


# acc: int - текущее значение
# next_el: int - следующий элемент
total = reduce(sum_custom, num, 10)  # 10 здесь начальное значение
print(total)
