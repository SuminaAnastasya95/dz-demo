a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a.union(b))


print(a & b)
print(a.intersection(b))


a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a - b)  # остаются те элементы, которые присутсвуют в а, но отсутствуют в b
print(b - a)  # остаются те элементы, которые присутсвуют в b, но отсутствуют в a


print(a ^ b)
# Исключаются общие, остаются только уникальные
print(a.symmetric_difference(b))
