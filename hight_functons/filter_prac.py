orders = [
    {"id": 1, "user": "Anton", "amount": 150, "status": "paid"},
    {"id": 2, "user": "Nastya", "amount": 50, "status": "canceled"},
    {"id": 3, "user": "Vikky", "amount": 250, "status": "paid"},
    {"id": 4, "user": "Edvard""", "amount": 350, "status": "draft"},
    {"id": 1, "user": "Anton", "amount": 150, "status": "paid"}
]


lists = list(filter(
    lambda o: o["amount"] > 100 and o["status"] == "paid", orders
))
print(lists)
