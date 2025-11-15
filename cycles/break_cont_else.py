for i in range(100):
    print(i)
    if i > 10:
        print("Конец цикла")
        break #Говорим, что мы прекращаем
print("Готово")
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# Конец цикла

for i in range(1, 11):
    if i % 2 == 1:
        continue #Прекращает текущую итиреацию цикла и продолжает следующую 
    print(i)
# 2
# 4
# 6
# 8
# 10

for i in range(5):
    print(i)
    if i > 3:
        break
else:
    print("Готово без break")