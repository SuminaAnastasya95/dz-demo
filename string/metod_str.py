password = "Hello Anastasya"
print(password.count("a")) #Вхождение конкретного значения описанного в count("") в значение. Регистрозависимо!!!
print(password.endswith("a")) #Проверка, что заканчивается с опредленного значения
print(password.startswith("h")) #Проверка, что начинается с опредленного значения
print("-"*20)
print(password.find("o")) #Поиск индекса ПЕРВОГО ВСТРЕЧАЮЕЩЕГОСЯ значения 
print(password.find("a", 6)) #Поиск индекса ПЕРВОГО ВСТРЕЧАЮЕЩЕГОСЯ значения, после указанного значения индекса. Т.е. будет искать индекс "а", который следует после 6 значения т.е. "А"
print("-"*20)
print(password.find("!")) #Если он не находит начения, то будет возвращать -1
print(password.index("o")) #Работает аналогоично .find
print("-"*20)
print(password.rfind("y")) #Работает аналогоично .find, только поиск осуществляется справа 
print(password.rindex("a")) #Работает аналогоично .find, только поиск осуществляется справа 


print("-"*20)
print(password.isnumeric()) #Все, что начинается с .is____ это проверка, что значение является каким-то. В данном случае проверка, что это число
print("123".isnumeric())

print("-"*20)
t = password.split("a")
print(t)

print("-"*20)
role = ("Admin", "User")
all_rolse = " ".join(role) #Каким символом хотим " " соединить, потом что соединяем .join(role)
print(all_rolse)