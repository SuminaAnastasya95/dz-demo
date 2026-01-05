# Задача 1: map() и квадраты
# Дан список: nums = [1, 2, 3, 4, 5]
# Получи список квадратов с помощью map() и lambda.

nums = [1, 2, 3, 4, 5]
new_nums = map(lambda e: e**2, nums)
print(list(new_nums))
