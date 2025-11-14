import random

round_count = int(input("Введите число раунодов: "))
pc = ("камень", "ножницы", "бумага")
pc_score = 0
user_score = 0
for r in range(1, round_count + 1):
    print(f"\nРайунд{r}")
    selection = input("Что выбираете (камень/ ножницы/ бумага):  ")
    if selection not in pc:
        print("Не корректный ввод")
        exit()
    pc_select = random.choice(pc)
    print(f"Компьтер выбрал: {pc_select}")
    if selection ==  pc_select:
        print('ничья')
    elif (selection == "камень" and pc_select == "ножницы") or \
          (pc_select == "камень" and selection == "бумага") or \
            (selection == "ножницы" and pc_select == "бумага"):
        print("Выйграл человек")
        user_score += 1
    else:
        print("Выйграл ПК")
        pc_score += 1
print("===Итог игры====")
print(f"Счет человека: {user_score}")
print(f"Счет компьютера: {pc_score}")

if user_score > pc_score:
    print("Ты победил!")
if user_score < pc_score:
    print("ПК победил!")
else:
    print("Ничья!")