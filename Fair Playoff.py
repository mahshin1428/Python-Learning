t = int(input())

for _ in range(t):
    s = list(map(int, input().split()))
    sort = sorted(s)

    if max(s[0], s[1]) == sort[2] or max(s[2], s[3]) == sort[2]:
        print("YES")
    else:
        print("NO")

