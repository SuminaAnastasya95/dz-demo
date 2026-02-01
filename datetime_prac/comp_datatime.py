import datetime


d1 = datetime.date(2025, 9, 17)
d2 = datetime.date(2025, 10, 17)
d3 = datetime.date(2025, 10, 17)
# d4 = datetime.datetime(2025, 10, 17)
print(d1 < d2)
print(d1 == d2)
print(d1 > d2)
# print(d3 < d4) в таком случае булеттоишбка, потому что мы не можем сравнивать разыне типы

now = datetime.datetime.now()
deadline = datetime.datetime(2025, 10, 12, 18, 0, 0)

if now < deadline:
    print("Еще успеваю")
else:
    print("Опоздала")
