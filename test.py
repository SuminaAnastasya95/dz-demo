
class BookError(Exception):
    """Общая ошибка по библиотеке"""
    pass


class NotFilterError(BookError):
    """Не передан текст фильтра"""
    pass


class NotCommandError(BookError):
    """Передана кривая команда"""
    pass


class InvalidParamSorted(BookError):
    """Передан кривой параметр сортировки"""
