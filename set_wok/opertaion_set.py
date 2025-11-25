s = {1, 2, 3, 4, 5, 4}
s.add(55)
print(s)


s.update([11, 8])
print(s)

s.remove(2)
print(s)
# s.remove(7) #не безопасно, потому что бросает ошибку если такого элемента нет

s.discard(7)  # безопасно, потому что НЕ бросает ошибку если такого элемента нет
s.discard(3)
print(s)

remove_items = s.pop()  # Удлаение элемента первого из хеш таблицы
print(remove_items)  # Возвращает, то какой элемент был удален
print(s)

print(4 in s)
print(86 in s)


for el in s:
    print(el)
