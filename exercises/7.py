def gen(n):
    for i in range(0, n, 2):
        yield i

n = int(input())
print(*gen(n), sep=",")