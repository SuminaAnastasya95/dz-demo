# Оставь только пате и salary
# Оставь только активных
# Их отсортируй по уменьшения зарплаты и выведи
# Посчитай сумму для выплат
from functools import reduce


employees = [
    {"name": "Anton", "department": "IT", "salary": 120000, "active": True},
    {"name": "Kate", "department": "HR", "salary": 90000, "active": False},
    {"name": "Oleg", "department": "IT", "salary": 150000, "active": True},
    {"name": "Maria", "department": "Finance", "salary": 110000, "active": True},
    {"name": "Ivan", "department": "IT", "salary": 95000, "active": False},
    {"name": "Dasha", "department": "Finance", "salary": 130000, "active": True}
]


def result_emplouees(employees: list):
    resul_empl = []
    for employr in employees:
        if employr["active"] == True:
            resul_empl.append(employr)
            employr.pop("department")
            employr.pop("active")
    return resul_empl

# sorted_one = sorted(result_emplouees, key=lambda e: -e["salary"])
# print(sorted_one)


active = filter(lambda e: e["active"], employees)
mapped = map(lambda e: {"name": e["name"], "salary": e["salary"]}, active)
sorted_emp = sorted(mapped, key=lambda e: -e["salary"])
print(sorted_emp)
total_salary = reduce(lambda acc, e: acc+e["salary"], sorted_emp, 0)
print(f"Суммарная зп: {total_salary}")
