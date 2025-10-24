# Проверить является ли введенное слово Палидромом
# Да - Торор, шалаш, мадам
# Нет - Привет, лакомство

word = input("Введите слово: ").lower()
invertedWord = word[::-1]

if word == invertedWord:
    print("Палидромом")
else:
    print("No Палидромом")    