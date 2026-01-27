import datetime


now = datetime.datetime.now()
print(now)
today = datetime.date.today()
print(today)
current_time = now.time()
print(current_time)

d = datetime.date(2025, 9, 17)
print(d.weekday())
print(d)
t = datetime.time(19, 0, 45)
print(t)
dt = datetime.datetime(2025, 9, 17, 19, 0, 45)
print(dt)
