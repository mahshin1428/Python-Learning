t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    m = 0
    for i in range(n):
        if a[i] == 0:
            count += 1
        else:
            m = max(m, count)
            count = 0

    m = max(m, count)
    print(m)

