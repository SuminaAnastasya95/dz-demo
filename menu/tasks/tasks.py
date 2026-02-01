from typing import TypedDict, Optional
from datetime import date

PRIORITIES = ["low", "med", 'high']


class Tasks(TypedDict):
    id: int
    title: str
    priority: str
    due: Optional[date]
    tags: Optional[list[str]]
    status: str


# t: Tasks = {
#     "id": 1,
#     "title": "Протереть пыль",
#     "priority": "low",
#     "status": "new",
#     "tags": ["home"]
# }


def make_task(id_: int, title: str, priority: str = 'med', due: Optional[date] = None, status: str = "now", tags: Optional[list[str]] = None) -> Tasks:
    if priority not in PRIORITIES:
        raise ValueError(
            "Не правильный приоритет. Возможны только 'low', 'med', 'high'")
    task: Tasks = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "due": due,
        "status": "new",
        "tags": tags
    }

    return task
