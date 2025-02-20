def generator(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            print(i)
            yield i
n = int(input()) 
print(list(generator(n)))     