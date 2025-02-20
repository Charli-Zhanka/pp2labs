def generator(n):
    for i in range(0,n,2):
        yield i
n = int(input())
print(list(generator(n)))