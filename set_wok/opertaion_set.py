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


a = {1, 2}
b = {1, 2, 3}
# Проверка является ли множество a частью b
print(a.issubset(b))  # True
print(b.issubset(a))  # False


a = {1, 2}
b = {1, 2, 3}
c = {3, 1, 2}
# Проверка является ли множество b частью a. Т.е. тоже самое что и .issubset() только работает наоборот
print(a.issuperset(b))  # False
print(b.issuperset(a))  # True

print(c == b)  # True
print(c != b)  # False


a.clear()
print(a)

d = b.copy()
print(d == b)
