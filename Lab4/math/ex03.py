import math
a = int(input("number:"))
b = int(input("lenght:"))
print(" area of regular polygon.", str(math.floor(a * b ** 2 )/ (4 * math.tan((2* math.pi)/(2 * a)))) )