user = {"age": 37, "name": 1}
user["citu"] = "Moscow"

for key in user:
    print(key)
# age
# name

for key in user.keys():
    print(key)
# age
# name

for key, value in user.items():
    print(f"{key}:{value}")
# age:37
# name:1

for value in user.values():
    print(value)
# 37
# 1
