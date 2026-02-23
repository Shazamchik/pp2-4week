def gen(n):
    i = 0
    while i <= n:
        yield n
        n-=1
n = int(input())
print(*gen(n))