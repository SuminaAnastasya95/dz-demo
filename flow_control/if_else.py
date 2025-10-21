age = input("Введите ваш возраст: ")

if int(age) < 18:
    print("Вам меньше 18 лет")
else:
    if int(age) < 50:
        print("Вам от 18 до 50 лет")
    else:
        print("Вам больше 50 лет")
	

# if условие1:
#     ...
# elif условие2:      # "else if" — проверяется, если первое условие ложно
#     ...
# else:               # выполняется, если все условия ложны
#     ...

# score = 85

# if score >= 90:
#     grade = "Отлично"
# elif score >= 75:
#     grade = "Хорошо"
# elif score >= 60:
#     grade = "Удовлетворительно"
# else:
#     grade = "Неудовлетворительно"

# print("Оценка:", grade)


# age = 19
# if int(age) >= 18 and int(age) <= 65:
#     print("Возраст подходит для работы")

# is_raining = False
# if not is_raining:
#     print("Можно гулять без зонта")
# else:
#     print("No")