t = int(input())
count = 0
for _ in range(t):
    a, b = map(int, input().split())
    r = a % b
    if r == 0:
        print(count)
    else:
        count = b - r
        print(count)
        count = 0

