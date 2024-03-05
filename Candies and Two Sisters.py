t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        c = n//2 - 1
        print(c)
    else:
        c = (n - 1)//2
        print(c)
