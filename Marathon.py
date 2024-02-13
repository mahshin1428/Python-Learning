t = int(input())

count = 0
for _ in range(t):
    a, b, c, d = map(int,input().split())
    if a < b:
        count += 1
    if a < c:
        count += 1
    if a < d:
        count += 1
    print(count)
    count = 0
