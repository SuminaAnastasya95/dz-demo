numbers = [1, 2, 3, 4]

# Удвоить каждое число
doubled = map(lambda x: x * 2, numbers)
# print(list(doubled))  # → [2, 4, 6, 8]
# 💡 map() возвращает итератор — оберни в list(), чтобы увидеть.

# # squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
# for key in books.keys():
#     names_book.append(key)
books = {"История одиночества": "Джон Бойн",
         "Мальчик в полосатой пижаме": "Джон Бойн",
         "Гордость и предупреждение": "Джейн Остин",
         "Оно": "Стивин Кинг"}

list_book = map(lambda x: , books)
print(list(list_book))
