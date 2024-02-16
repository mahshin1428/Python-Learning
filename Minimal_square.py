t = int(input())

for _ in range(0, t):
    a, b = map(int, input().split())
    if a != b:
        m = max(max(a, b), min(a, b) * 2)
        ans = m ** 2
        print(ans)
    if a == b:
        m = 2 * b
        ans = m ** 2
        print(ans)

