import datetime
now = datetime.datetime.now()
# %Y - 2025 год
# %y - 25 год
# %m - 08 месяцы
# %d - 19 дни
# %H - 24 часы
# %M - 24 минуты
# %S - 02 секунды

print(now.strftime("%Y-%m-%d"))
# print(now.strftime("%Y/%m/%d"))
print(now.strftime("%Y-%m-%d %H:%M:%S"))

s = '2025-09-07 18:44'
dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
print(dt)
