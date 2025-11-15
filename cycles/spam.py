# Если есть слово СПАМ, останавливаем проверку
# Если сщщбщение больше 20 символов - прокускаем его
# Вывести в результате был ли спам
messeges = [
    "Привет!",
    "Купи дешевые крусы", 
    "Как дела?", 
    "СПАМ реклама",
    "Пойдем играть в футбол"
]


for i in messeges:
    low_messeges = i.lower()
    if len(low_messeges) > 20:
        print(f"В сообщении более 20 символов - {low_messeges}")
        continue
    if low_messeges.count("спам"):
        print(f"Найден спам: {low_messeges}")
        break
else:
    print("Спам НЕ найден")
