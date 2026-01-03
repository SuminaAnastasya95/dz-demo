import sys

books = {
    "История одиночества": "Джон Бойн",
    "Мальчик в полосатой пижаме": "Джон Бойн",
    "Гордость и предубеждение": "Джейн Остин",
    "Оно": "Стивен Кинг"
}

if len(sys.argv) < 2:
    print("Ошибка: не указан action (filter или sort)")
    sys.exit(1)

action = sys.argv[1]

if action == "filter":
    requested = sys.argv[2:]  # безопасно: срез не вызывает IndexError
    filtered = filter(lambda title: title in books, requested)
    result = map(lambda title: f"{title} — {books[title]}", filtered)
    for line in result:
        print(line)

elif action == "sort":
    if len(sys.argv) < 3:
        print("Ошибка: для sort требуется указать 'book' или 'author'")
        sys.exit(1)

    sort_by = sys.argv[2]

    if sort_by == "book":
        def key_func(pair): return pair[0].lower()
    elif sort_by == "author":
        def key_func(pair): return pair[1].lower()
    else:
        print("Ошибка: sort_by должен быть 'book' или 'author'")
        sys.exit(1)

    # Получаем отсортированные пары (книга, автор)
    sorted_pairs = sorted(books.items(), key=key_func)

    # Формируем строки с помощью map
    result = map(lambda pair: f"{pair[0]} — {pair[1]}", sorted_pairs)

    for line in result:
        print(line)

else:
    print(
        f"Ошибка: неизвестный action '{action}'. Используйте 'filter' или 'sort'")
    sys.exit(1)
