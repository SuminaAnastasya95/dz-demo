role = input("Введите роль: ")
a = 5
# if role == "admin":
#     print("admin")
# elif role == "manager":
#     print("manager")
# elif role == "seo":
#     print("soe")
# else:
#     print("who are you?")

# Mach/ case

# Рекомендации:
# Match-case лучше подходит для небольших списков значений, когда требуется структура и читаемость.
# Для более сложных условий, включая дополнительные проверки, классический if-elif-else может оказаться более подходящим.
# Обязательно включение дефолтного кейса для обработки всех возможных значений.

# Выбираем какую переменную хотим сравнить
# а дальше в case передаем, то мы сравниваем
# case _ - работает как и else
match role:
    case "admin" | "ADMIN" if a > 0:  # где | = or + можно добавить условие if a > 0
        print("admin")
    case "manager":
        print("manager")
    case "seo":
        print("seo")
    case _:
        print("Who are you?")


match a:
    case a if a > 0:
        print(">0")
    case _:
        print("<=0")
