numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rez = 0
for i in numbers:
    if i % 2 == 0:
        rez += i
print(rez)


sum_res = sum(i for i in numbers if i % 2 == 0)
print(sum_res)


# even_sum = sum(x for x in range(1, 101) if x % 2 == 0)
