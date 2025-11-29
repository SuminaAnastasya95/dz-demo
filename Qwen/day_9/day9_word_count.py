# Напиши функцию count_words(text), которая:

# разбивает текст на слова (по пробелам),
# возвращает словарь: слово → количество вхождений.
# Пример:
# count_words("hello world hello")
# # → {"hello": 2, "world": 1}
#  Используй .split() и цикл.
# lists = []


def count_words(text):
    split_text = text.split(" ")
    dictionary = {}
    for key in split_text:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary


print(count_words("hello world hello"))
