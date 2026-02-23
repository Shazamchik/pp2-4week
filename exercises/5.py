import datetime 
def func(d1, d2):
    timedelta = d2 - d1
    return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.datetime(2022, 10, 5)
date2 = datetime.datetime.now()
print(func(date1, date2))
