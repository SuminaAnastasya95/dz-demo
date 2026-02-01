from zoneinfo import ZoneInfo
from datetime import datetime


now_utc = datetime.now(ZoneInfo("UTC"))
now = datetime.now()
print(now)
print(now_utc)


now_ny = datetime.now(ZoneInfo("America/New_York"))
print(now_ny)


meeting = datetime(2025, 9, 17, 12, 0, 0, tzinfo=ZoneInfo("Europe/Moscow"))
meeting_ny = meeting.astimezone(ZoneInfo("America/New_York"))
print(meeting_ny)
