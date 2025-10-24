floor = int(input("Введите номер этажа: "))

match floor:
    case -1:
        print("Подвал: здесь находится склад")
    case 1:
        print("Холл и ресепшен")
    case floor if floor >= 2 and floor <= 9:
    #можно написать и так: case _ if 2 <= floor <= 9:
        if floor % 2 == 0:
            print("Офисный этаж")
        else:
            print("Жилой этаж")
    case 10:
        print("Технический этаж вход запрещен")
    case _:
        print("Такого этажа нет")