from command.help_menu import help_commands


def main():
    print("Таск менеджер. help - для справки")
    while True:
        try:
            raw = input(">").strip()
            parts = raw.split()
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    kind_help = input(
                        "С какой командой помочь?\nlist\nadd\nremove\nedit\ntags\nexit\n>>")
                    help_commands(kind_help)
                case "list":
                    pass
                case "add":
                    pass
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


main()
