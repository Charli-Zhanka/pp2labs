import datetime
a = datetime.datetime.now()
b = a.replace(hour=16)
print((a-b).total_seconds())