import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎮 Я загадал число от 1 до 10. Попробуй угадать!")

while True:
    attempts += 1
    user_input = input("Ваша попытка: ")
    
    # Проверка, что введено число
    if not user_input.isdigit():
        print("❌ Ошибка: введите целое число!")
        continue
    
    user_num = int(user_input)
    
    # Проверка диапазона
    if user_num < 1 or user_num > 10:
        print("❌ Число должно быть от 1 до 10!")
        continue
    
    # Сравнение
    if user_num < secret_number:
        print("⬆️ Больше!")
    elif user_num > secret_number:
        print("⬇️ Меньше!")
    else:
        print(f"🎉 Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
        break