numbers = [1, 2, 3, 4]

# Удвоить каждое число
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # → [2, 4, 6, 8]
# 💡 map() возвращает итератор — оберни в list(), чтобы увидеть.
