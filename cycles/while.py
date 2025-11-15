# обычно используются для повторения неизвестного числа раз, что полезно, когда число итераций зависит от заданного условия.
# Цикл while работает до того момента пока он не будет возвращать False
count = 1
while count <= 3:
    print(count)
    count += 1

# Угадай число
secret_number = 7
guess = 0
print("Угадай число от 1 - 10")

while guess != secret_number:
    guess = int(input("Ведите число: "))
    if guess < secret_number:
        print("Загаданное число больше")
    elif guess > secret_number:
        print("Загаданное число меньше")
print("Ты угадал!")