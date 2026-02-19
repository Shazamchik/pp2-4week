def gen(n):
    x = 1
    while x <= n:
        yield x*x
        x+=1
n = int(input())
nums = gen(n)
for i in nums:
    print(i)