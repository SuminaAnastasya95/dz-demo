import sys

# Если action == "filter" - С помощью filter выбери книги переданные в sys.argv[2]. С помощью map выведи список строк "Книга — Автор".

# Если action == "sort" - С помощью map подготовь список строк "Книга — Автор". Отсортируй список по алфавиту в зависимости от author или book.


books = {
    "История одиночества": "Джон Бойн",
    "Мальчик в полосатой пижаме": "Джон Бойн",
    "Гордость и предубеждение": "Джейн Остин",
    "Оно": "Стивен Кинг"
}
if sys.argv[1] == "filter":
    requested = sys.argv[2:]
    filter_book = filter(lambda title: title in books, requested)
    # print(list(filter_book))
    result = list(map(lambda title: f"{title} - {books[title]}", filter_book))
    # print(result)
    for line in result:
        print(line)
elif sys.argv[1] == "sort":
    sort_by = sys.argv[2]  # "book" или "author"

    # Шаг 1: с помощью map создаём список строк "Книга — Автор"
    items = list(map(lambda title: (title, books[title]), books.keys()))
    lines = list(map(lambda pair: f"{pair[0]} — {pair[1]}", items))

    # Но для сортировки удобнее сначала отсортировать пары (книга, автор),
    # а потом применить map — так мы сможем сортировать по нужному полю

    # Пересоздадим: работаем с парами (title, author)
    book_author_pairs = list(books.items())  # [('Книга', 'Автор'), ...]

    if sort_by == "book":
        sorted_pairs = sorted(book_author_pairs, key=lambda x: x[0].lower())
    elif sort_by == "author":
        sorted_pairs = sorted(book_author_pairs, key=lambda x: x[1].lower())
    else:
        raise ValueError("sort_by должен быть 'book' или 'author'")

    # Теперь map для формирования строк
    result = map(lambda pair: f"{pair[0]} — {pair[1]}", sorted_pairs)

    # Выводим
    for line in result:
        print(line)
