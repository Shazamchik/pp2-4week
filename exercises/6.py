def gen(n):
    x = 1 
    while x<=n:
        yield x**2
        x+=1
n = int(input())
sq = gen(n)
for i in sq:
    print(i)