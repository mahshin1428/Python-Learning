t = int(input())

for _ in range(t):
    st = list(input())
    if len(st) % 2 != 0:
        print("NO")
    else:
        x = len(st)//2
        f = st[:x]
        s = st[x:]
        if f == s:
            print("YES")
        else:
            print("NO")

