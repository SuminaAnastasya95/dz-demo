"""Модуль для добавления команд"""
from tasks.tasks import Tasks, make_task
from command.args import parss_add
from command.table import stringigy_tamble


def add_command(tasks: list[Tasks], args: list[str], next_id: int) -> int:
    try:
        title, prio, due, tags = parss_add(args)
        task = make_task(1, title, prio, due, tags)
        tasks.append(task)
        print("Добавлена задача")
        print(stringigy_tamble([task]))
    except ValueError as e:
        print(f"Ошибка - {e}")
        return next_id
