books = {"История одиночества": "Джон Бойн",
         "Мальчик в полосатой пижаме": "Джон Бойн",
         "Гордость и предупреждение": "Джейн Остин",
         "Оно": "Стивин Кинг"}

print(f"Список авторов: ", set(books.values()))
names_book = []
for key in books.keys():
    names_book.append(key)
print(f"Список книг: ", names_book)
