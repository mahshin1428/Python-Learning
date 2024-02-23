n = int(input())
a = list(map(int, input().split()))
m = max(a)

e = 0
c = 0
for i in range(len(a)):
    c = m - a[i]
    e += c

print(e)
