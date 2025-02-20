import datetime
a = datetime.datetime.now()

def drop(a):
    ds = a.replace(microsecond = 0)
    return ds
print(drop(a))