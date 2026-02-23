import datetime
x = datetime.datetime.now()
newx = x.replace(microsecond = 0)
print(x)
print(newx)