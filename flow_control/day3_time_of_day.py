# Спрашивает у пользователя час (целое число от 0 до 23)
# Выводит:
# "Доброе утро!" — с 6 до 11
# "Добрый день!" — с 12 до 17
# "Добрый вечер!" — с 18 до 23
# "Доброй ночи!" — с 0 до 5

whatIsTime = int(input("Сколько время? "))
if 6 <= whatIsTime and whatIsTime <= 11:
    print("Доброе утро!")
elif 12 <= whatIsTime and whatIsTime <= 17:
    print("Добрый день!")
elif 18 <= whatIsTime and whatIsTime <= 23:
    print("Добрый вечер!")
elif 0 <= whatIsTime and whatIsTime <= 5:
    print("Доброй ночи!")
else:
    print("Что-то не то")