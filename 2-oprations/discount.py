food = input("Сколько потратили на еду: ")
transport = input("Сколько потратили на транспорт: ")
inter = input("Сколько потратили на развлечения: " )

foodInt = int(food)
transportInt = int(transport)
interInt = int(inter)

print("Потраченная сумма составляет: ", (foodInt + transportInt + interInt))
print("Среднее значение потраченной суммы: ", (foodInt + transportInt + interInt)/ 3)