try:
    x = int(input("Введите число: "))
    print(10/0)
# except ValueError:
#     print("Ошибка input")
# except ZeroDivisionError:
#     print("Ошибка деления на ноль")
# else:
#     print("Нет ошибок")
except Exception as e:  # Будет обрабатывать все ошибка не в зависимости от того что это за ошибка
    print("Ошибка: ", e)
finally:  # Позволяет выполннить код не зависимо от того была ли ошибка или ее не было, эта часть будет работаь всегда
    print("Финал")
print("Продолжение...")
