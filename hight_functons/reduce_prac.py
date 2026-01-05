# 1. Получить общую сумму всех заказов
# 2. Кол-во всех проданных заказов


from functools import reduce


orders = [
    {"id": 1, "user": "Anton", "items": [
        {"name": "Laptop", "price": 1000},
        {"name": "Mouse", "price": 50}
    ]},
    {"id": 2, "user": "Kate", "items": [
        {"name": "Phone", "price": 700}
    ]},
    {"id": 3, "user": "Oleg", "items": [
        {"name": "Monitor", "price": 300},
        {"name": "Keyboard", "price": 100}
    ]}
]


def aggregate_simple(orders: list):
    sum_price = 0
    for order in orders:
        for items in order["items"]:
            sum_price += items['price']
    lens = 0
    name_items = []
    for order in orders:
        # print(order)
        for items in order["items"]:
            lens += 1
            if items["name"] not in name_items:
                name_items.append(items["name"])
    return sum_price, lens, name_items


sum_price, lens, name_items = aggregate_simple(orders)
print(f"Колличество проданных товаров: {sum_price}")
print(f"Колличество проданных товаров: {lens}")
print(f"Проданные товары: {name_items}")


def aggregate(accumulator: dict, order: dict) -> dict:
    order_sum = sum(item["price"] for item in order["items"])
    order_count = len(order["items"])
    return {"total_price": accumulator["total_price"] + order_sum,
            "total_count": accumulator["total_count"] + order_count}


result = reduce(aggregate, orders, {"total_price": 0, "total_count": 0})
print(result)
