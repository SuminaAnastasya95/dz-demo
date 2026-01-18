def help_commands(kind_help):
    try:
        if kind_help == "add":
            print("Осуществляется добавление таски в формате:\n"
                  "< title > priority=low | med | high [YYYY-MM-DD] [tags=a, b, c] - Добавить")
        elif kind_help == "list":
            print("Отображается список всех задач")
        elif kind_help == "remove":
            print("Осуществляется удаление\n<id> - Удалить")
        elif kind_help == "edit":
            print(
                "Осуществляется изменение\n<id> [title=...] [priority=...] due=[YYYY-MM-DD] - Изменить")
        elif kind_help == "tags":
            print(
                "Осуществляется добавление тега\n<id> add|remove <tag> - Добавление тега")
        elif kind_help == "help":
            print("Помощь")
        elif kind_help == "exit":
            print("Выход из программы")
        elif kind_help not in ["add", "list", "remove", "edit", "tags", "exit", "help"]:
            print("Такая команда отсутствует")
    except Exception as e:
        print("[ERROR] - ", e)


# remove\nedit\ntags\nexit
