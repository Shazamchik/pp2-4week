n = int(input())
squares = (x*x for x in range(1, n+1))
for i in squares:
    print(i)