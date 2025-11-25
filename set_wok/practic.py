# Уникальные визиты
# найти ид кто поситил оба дня
# найти ид кто посетил только один день
# айти ид кто посетил только второй день
# найти ид кто был только 1 раз

visitors_day1 = [101, 102, 103, 101, 104, 102, 105, 101]
set_day1 = set(visitors_day1)
visitors_day2 = [101, 108, 100, 101, 104, 102]
set_day2 = set(visitors_day2)

print("Уникальные поситители: ")
print(set_day1 | set_day2)

print("Кто посетил оба дня")
print(set_day1 & set_day2)

print("Кто посетил только первый день")
print(set_day1 - set_day2)

print("Кто посетил только второй день")
print(set_day2 - set_day1)

print("Кто посетил только один раз: ")
print(set_day1 ^ set_day2)
