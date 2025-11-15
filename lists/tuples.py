#Не можем менять внутренние элементы
t = (1,2,3,4)
t1 = 1,2,3,4
# print(type(t1)) #<class 'tuple'>
print(t[1])

#Не изменяем
# t[0] = 7   TypeError: 'tuple' object does not support item assignment

t2 = (1, "2", [55, 3])
print(t2[-1][0])
t2[-1][0] = 8 #Изменение списка внутри кортежа
print(t2)
print(len(t2))


# Преобразование кортежа в список
l = list(t)
print(l)

# Преобразование списка в кортеж
list2 = [12, 25, 66]
tuple2 = tuple(list2)
print(tuple2)