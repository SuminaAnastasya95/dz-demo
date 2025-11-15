#Строки такие же последовательности символов
name = "Anastasya"
print(type(name))
print(name[0])
# print(name[25]) IndexError: string index out of range
# name[0] = "R" Ошибка не можем менять 
print(len(name))

t = tuple(name)
print(t)
l = list(name)
print(l)

sep = "=" * 20
print(sep)

sep2 = (1, 2)* 20
print(sep2)