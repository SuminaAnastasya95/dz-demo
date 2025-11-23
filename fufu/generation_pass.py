import random
import string

# 1. Показать пароль
# 2. Добавить пароль
# 3. Удалить пароль
# 4. Обновить пароль
# 5. Выход


def generation_pass(length: int = 8, use_symbols: bool = True):
    if length < 3:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+?"
    pool = letters + digits + (symbols if use_symbols else "")

    password_chars: list[str] = []
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))
    return "".join(password_chars)


# print(generation_pass())
# print(generation_pass(10, False))

passwords = {}
# ключ: строка (домен) и значение: строка (пароль)
# {"purpleshcool.ru":"1234"}


def menu(passwords: dict):
    while True:
        print("1. Показать пароль\n"
              "2. Добавить пароль\n"
              "3. Удалить пароль\n"
              "4. Обновить пароль\n"
              "5. Выход\n")
        user_choise = input("Выбирите меню: ->")
        int_user_choise = int(user_choise)
        if not int_user_choise in (1, 2, 3, 4, 5):
            print("Выбирите пункт меню из 1, 2, 3, 4, 5")
        elif int_user_choise == 5:
            print("Выход, до свидания!")
            exit()
        elif int_user_choise == 1:
            show_pass(passwords)
        elif int_user_choise == 2:
            add_pass(passwords)
        elif int_user_choise == 3:
            delete_passwords(passwords)
        elif int_user_choise == 4:
            update_password(passwords)


def show_pass(password):
    print(password)


def add_pass(password):
    print("Какой домен?")
    domen = input("->")
    password[domen] = generation_pass()
    print(password)


def delete_passwords(password):
    print(password)
    user_select = input("Какой элемент удалить? Введите в формате ключа:  ")
    if not user_select in password:
        print("Такого домена нет в спике!")
    else:
        password.pop(user_select)
        print(password)


def update_password(password):
    update_domene = input("У какого домена хотите обновить пароль? ")
    if not update_domene in password:
        print("Такого домена нет в спике!")
        exit()
    else:
        password[update_domene] = generation_pass()
        print(password)


menu(passwords)
