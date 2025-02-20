import datetime
a = datetime.datetime.now()
b = a - datetime.timedelta(1)
c = a + datetime.timedelta(1)
print("Yesterday: " + str(b))
print("Today: " + str(a))
print("tomorrow: " + str(c))