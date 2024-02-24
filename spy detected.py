t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    u = [e for e in a if a.count(e) == 1]
    i = a.index(u[0])
    print(i+1)

