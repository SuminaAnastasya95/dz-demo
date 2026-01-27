from typing import TypedDict
import random

PRIORITIES = ["low", "med", 'high']


class Tasks(TypedDict):
    id: int
    title: str
    priority: str
    tags: list[str]
    status: str


# t: Tasks = {
#     "id": 1,
#     "title": "Протереть пыль",
#     "priority": "low",
#     "status": "new",
#     "tags": ["home"]
# }


def make_task(id_: int, title: str, priority: str, status: str = "med", tags: list[str] = []) -> Tasks:
    if priority not in PRIORITIES:
        raise ValueError(
            "Не правильный приоритет. Возможны только 'low', 'med', 'high'")
    task: Tasks = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "status": "new",
        "tags": tags
    }

    return task
