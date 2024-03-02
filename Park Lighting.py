t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = n*m
    if a % 2 == 0:
        light = a // 2
    else:
        light = (a+1) // 2

    print(light)
