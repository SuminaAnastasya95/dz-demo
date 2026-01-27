import datetime

new_year = datetime.date(2027, 1, 1)
today = datetime.date.today()
diff = new_year - today
print(diff)
print(diff.days)


next_week = today + datetime.timedelta(weeks=1)
print(next_week)
next_week = today + datetime.timedelta(days=7)
print(next_week)
last_month = today - datetime.timedelta(days=30)
print(last_month)
