nums = [5, 2, 9, 1, 7]
print(sorted(nums))
print(sorted(nums, reverse=True))

words = ["banana", "apple", "lime"]
print(sorted(words))

user = [
    {"name": "Anton", "age": 18},
    {"name": "Marry", "age": 20},
    {"name": "Peter", "age": 10},
    {"name": "Anna", "age": 20},
    {"name": "Bella", "age": 46}
]
print(sorted(user, key=lambda u: u["age"]))
print(sorted(user, key=lambda u: (u["age"], u["name"])))
# В обратном порядке по возрасту, но в прямом порядке по имени
print(sorted(user, key=lambda u: (-u["age"], u["name"])))
