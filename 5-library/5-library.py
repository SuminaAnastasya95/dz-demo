import sys


# === 1. Объявляем базовый класс ошибки ===
class CLIError(Exception):
    """Базовый класс для всех ошибок командной строки."""
    pass


# === 2. Расшираем его специфичными ошибками ===
class MissingActionError(CLIError):
    pass


class UnknownActionError(CLIError):
    pass


class InvalidSortParamError(CLIError):
    pass


class MissingFilterArgsError(CLIError):
    pass


books = {
    "История одиночества": "Джон Бойн",
    "Мальчик в полосатой пижаме": "Джон Бойн",
    "Гордость и предубеждение": "Джейн Остин",
    "Оно": "Стивен Кинг"
}
try:
    if len(sys.argv) < 2:
        raise MissingActionError(f"Передан кривой параметр сортировки")
        # print("Ошибка: не указан action (filter или sort)")
        # sys.exit(1)

    action = sys.argv[1]

    if action == "filter":
        if len(sys.argv) < 2:
            raise MissingFilterArgsError()

        requested = sys.argv[2:]  # безопасно: срез не вызывает IndexError
        filtered = filter(lambda title: title in books, requested)
        filter_list = list(filtered)
        if not filter_list:
            raise MissingFilterArgsError(
                "Ни одна из указанных книг не найдена")
        result = map(lambda title: f"{title} — {books[title]}", filtered)
        for line in result:
            print(line)

    elif action == "sort":
        if len(sys.argv) < 3:
            raise InvalidSortParamError(
                "Ошибка: для sort требуется указать 'book' или 'author'")

        sort_by = sys.argv[2]

        if sort_by == "book":
            def key_func(pair): return pair[0].lower()
        elif sort_by == "author":
            def key_func(pair): return pair[1].lower()
        else:
            raise InvalidSortParamError(
                "Ошибка: sort_by должен быть 'book' или 'author'")

        # Получаем отсортированные пары (книга, автор)
        sorted_pairs = sorted(books.items(), key=key_func)

        # Формируем строки с помощью map
        result = map(lambda pair: f"{pair[0]} — {pair[1]}", sorted_pairs)

        for line in result:
            print(line)

    else:
        raise MissingActionError(
            f"Ошибка: неизвестный action '{action}'. Используйте 'filter' или 'sort'")

except MissingActionError:
    print("Ошибка не указано действие(filter или sort)", file=sys.stderr)
    sys.exit(1)
except UnknownActionError as e:
    print(f"Ошибка - {e}", file=sys.stderr)
    sys.exit(1)
except InvalidSortParamError as e:
    print(f"Ошибка - {e}", file=sys.stderr)
    sys.exit(1)
