import random


def select_variant():
    selection = None
    while selection not in pc:
        selection = input("Что выбираете (камень/ ножницы/ бумага): ")
        if selection not in pc:
            print("Попробуй еще раз")
    return selection


def compute_game_result(user_ch: str, comp_ch: str):
    if user_ch == comp_ch:
        print('ничья')
        return (0, 0)
    elif (user_ch == "камень" and comp_ch == "ножницы") or \
        (comp_ch == "камень" and user_ch == "бумага") or \
            (user_ch == "ножницы" and comp_ch == "бумага"):
        print("Выйграл человек")
        return (1, 0)
    else:
        print("Выйграл ПК")
        return (0, 1)


def print_result(user_result: int, pc_result: int):
    print("===Итог игры====")
    print(f"Счет человека: {user_result}")
    print(f"Счет компьютера: {pc_result}")
    if user_result > pc_result:
        print("Ты победил!")
    if user_result < pc_result:
        print("ПК победил!")
    else:
        print("Ничья!")


round_count = int(input("Введите число раунодов: "))
pc = ("камень", "ножницы", "бумага")
pc_score = 0
user_score = 0

for r in range(1, round_count + 1):
    print(f"\nРайунд{r}")
    selection = select_variant()
    pc_select = random.choice(pc)
    print(f"Компьтер выбрал: {pc_select}")
    [user_mod, comp_mod] = compute_game_result(selection, pc_select)
    user_score += user_mod
    pc_score += comp_mod

print_result(user_score, pc_score)
