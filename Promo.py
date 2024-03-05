n, q = map(int, input().split())

p = list(map(int, input().split()))
p.sort(reverse=True)

for _ in range(q):
    cost = 0
    x, y = map(int, input().split())
    for i in range(x):
        if i >= x - y:
            cost += p[i]

    print(cost)
