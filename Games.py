n = int(input())

hc = []
ac = []

for _ in range(n):
    h, a = map(int, input().split())
    hc.append(h)
    ac.append(a)

count = 0
for i in range(n):
    if hc[i] in ac:
        count += ac.count(hc[i])

print(count)
