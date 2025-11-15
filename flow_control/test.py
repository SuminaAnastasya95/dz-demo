# age = int(input("Введите возраст: "))
# match age:
#     case 0:
#         print("Ты еще не родился")
#     case _ if 0 <= age <= 17:
#         print("Child")
#     case _ if 18 <= age <= 69:
#         print("Adult")
#     case _ if 70 <= age <= 120:
#         print("Senior")
#     case _:
#         print("woo")

age = 10

if int(age) < 18:
print("Вам меньше 18 лет")
else:
    if int(age) < 50:
        print("Вам от 18 до 50 лет")
    else:
        print("Вам больше 50 лет")
	