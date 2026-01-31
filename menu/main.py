from shlex import split
from command.help_menu import help_commands
from tasks.tasks import make_task, Tasks
from command.add import add_command


def main():
    tasks: list[Tasks] = []
    next_id = 1
    print("Таск менеджер. help - для справки")
    while True:
        try:
            raw = input(">").strip()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    kind_help = input(
                        "С какой командой помочь?\nlist\nadd\nremove\nedit\ntags\nexit\n>>")
                    help_commands(kind_help)
                case "list":
                    pass
                case "add":
                    next_id = add_command(tasks, args, next_id)
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    break
                case _:
                    print("Не знаю такой команды")
        except KeyboardInterrupt:
            print("\nЗавершение приложение...")
            break
        except Exception as e:
            print("[ERROR] - ", e)


if __name__ == "__main__":
    # main()
    # r - чтение
    # w - запись
    # a - добавить
    # x - сщздание нового файла
    # b - бинарный файл
    # t - текстовый
    # + - открыть для чтения/ записи
    f = open("notes.txt", 'a', encoding='utf-8')
    f.write('Первая строка\n')
    f.write('Вторая строка\n')
    f.close()
