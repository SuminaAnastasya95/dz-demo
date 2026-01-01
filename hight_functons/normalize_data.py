users = [
    {"name": "anton", "age": "25"},
    {"name": "KATE", "age": " 25"},
    {"name": "OLeg", "age": "22"}
]


def normlize(user: dict[str, str]) -> dict:
    return {
        "name": user["name"].strip().capitalize(),
        "age": int(user["age"].strip())
    }


normalize_users = list(map(normlize, users))
print(normalize_users)
