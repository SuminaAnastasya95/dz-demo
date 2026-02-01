# 1. Открытие файла: open()
# Базовый синтаксис:
import json
file = open("filename.txt", mode="r", encoding="utf-8")
# ... работа с файлом
file.close()  # ← не забыть!

# Режимы (mode):
# Режим      Значение                   Можно
# 'r'        чтение (по умолчанию)      читать
# 'w'        запись                     писать (старое содержимое стирается!)
# 'a'        дозапись                   добавлять в конец
# 'r+'       чтение + запись            читать и писать
⚠️ Всегда указывай encoding = "utf-8" — иначе на Windows могут быть проблемы с кириллицей.

2. Контекстный менеджер with — лучший способ
Автоматически закрывает файл, даже если была ошибка:

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    # файл закроется сам после выхода из блока
✅ Всегда используй with — это стандарт де-факто.

Метод              Описание
f.read()           читает весь файл как строку
f.readline()       читает одну строку
f.readlines()      читает все строки → список
f.write("текст")   записывает строку(возвращает длину)
f.writelines(list) записывает список строк(без \n автоматически!)
📌 Пример записи:

with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Тест 1: passed\n")
    f.write("Тест 2: failed\n")

4. Работа с JSON(часто в API-тестах)


# Запись
data = {"name": "Анна", "age": 25}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Чтение
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# ensure_ascii=False — чтобы кириллица не экранировалась (\u0410\u043d\u043d\u0430 → "Анна").
