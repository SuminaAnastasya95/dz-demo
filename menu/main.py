def main():
    print("Таск менеджер. help - для справки")
    while True:
        try:
            raw = input(">").strip()
            parts = raw.split()
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
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
