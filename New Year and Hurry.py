n, k = map(int, input().split())
time = 240

t = 0
p = 0
for i in range(1, n+1):
    t += i * 5
    if t + k <= time:
        p += 1
    else:
        break

print(p)


