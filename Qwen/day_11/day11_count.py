# Напиши программу, которая:

# читает файл,
# считает количество строк и количество слов,
# выводит:
# "Строк: 5, Слов: 5"
# 💡 Подсказка: line.split() → список слов в строке.

with open("input.txt", "r", encoding="utf-8") as f:
    words = f.read()
    count_words = len(words.split())
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    count_lines = len(lines)
    print(count_lines)

print(f"Строк: {count_lines}, Слов: {count_words}")
