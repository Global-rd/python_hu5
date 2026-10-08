from datetime import datetime as dt
from datetime import timezone, timedelta

now = dt.now(timezone.utc)
print(now)
print(type(now))

#STRING TO DATE
date_string = "2026-10-08 19:09:08"
date_object = dt.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(type(date_object))

#DATE TO STRING

date_string = dt.strftime(date_object, "%Y-%m-%d %H:%M:%S")
print(date_string)

#adding 5 days difference to a datetime object

five_days = timedelta(days=5.5)
new_date = now + five_days
print(new_date)