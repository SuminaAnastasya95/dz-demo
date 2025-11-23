user = {"age": "37", "name": "Anastasya"}  # type: ignore
# empy = {}
# contry = dict(germany="Berlin", englang="Londan")
# pairse = dict({("a", 1), ("b", 2)})  # type: ignore
# print(pairse)
print(user["name"])  # Такая запись не всегда безопасна
user["age"] = "20"
print(user["age"])

# print(user["city"]) #Такая безопасная, потому что в этом варианте будет выведена ошибка
# В то время как это намного более выгодный вариант, потому что при таком выводе он вернет None
print(user.get("city", "Moscow"))
value = user.pop("age")  # Удаление элементов
print(value)
print(user)


exist = "name" in user  # Проверка наличия нужного ключа
print(exist)


user["12"] = "12"
print(user)


def add_pass(password):
    print("Какой домен?")
    domen = input("->")
    print("Какой ваш пароль?")
    user_pass = input("->")
    password[domen] = user_pass
    print(password)


password = {'lolo': 'lolo', 'pass': 'pass'}
add_pass(password)


def delete_passwords(password):
    print(password)
    user_select = input("Какой элемент удалить? Введите в формате ключа:  ")
    delete = password.pop(user_select)
    print(password)


delete_passwords(password)


def update_password(password):
    update_domene = input("У какого домена хотите обновить пароль?")
    update_value = input("Какое значение хотите обновит? ")
    password[update_domene] = update_value
    print(password)


update_password(password)
