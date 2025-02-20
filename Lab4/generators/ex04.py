a = int(input())
b = int(input())
def generator(a, b):
    for i in range(a, b):
        yield i * i
    for i in range(a, b):
        print(i*i, end = ",")
print()
print(list(generator(a, b)))