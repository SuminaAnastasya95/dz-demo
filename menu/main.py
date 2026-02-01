import json
from shlex import split
from command.help_menu import help_commands
from tasks.tasks import make_task, Tasks
from command.add import add_command
from storege.file import save_tasks, load_tasks


def main():
    file_tasks = 'tasks.json'
    tasks, next_id = load_tasks(file_tasks)
    file_path = 'tasks.json'
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
                    save_tasks(file_path, tasks)
                    break
                case _:
                    print("Не знаю такой команды")
        except KeyboardInterrupt:
            save_tasks(file_path, tasks)
            print("\nЗавершение приложение...")
            break
        except Exception as e:
            save_tasks(file_path, tasks)
            print("[ERROR] - ", e)


if __name__ == "__main__":
    main()
    # r - чтение
    # w - запись
    # a - добавить
    # x - создание нового файла
    # b - бинарный файл
    # t - текстовый
    # + - открыть для чтения/ записи
    # with open("notes.txt", 'w', encoding='utf-8') as f:
    #     f.write("Hello!\n")
    #     f.write("i can do it!\n")
    # print("Exit")
    # res = json.dumps({'a': True, 'b': [1, 2, 3]})
    # # print(res)
    # with open('task.json', 'w', encoding='utf-8') as f:
    #     json.dump({"id": 1, "title": "jdjdjd"}, f, ensure_ascii=False,
    #               indent=2)
    # with open("notes.txt", 'r', encoding='utf-8') as f:
    #     # text = f.read()
    #     # print(text)
    #     for line in f:
    #         print(">", line.rstrip())

    # with open("tasks.json", 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    #     print(data)
