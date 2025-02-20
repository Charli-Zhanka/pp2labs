def generator(n):
    for i in range(n):
        s = i * i
        yield s
n = int(input())
print(list(generator(n)))