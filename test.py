import datetime

dt = datetime.datetime.now()
d_truncated = datetime.date(dt.year, dt.day, dt.month)
days = [d_truncated]
for i in range(0,5):
    next_day = d_truncated + datetime.timedelta(days=1)
    days.append(next_day)
    d_truncated = next_day

for i in range(len(days)):
    print(days[i])