n = int(input())

s = list(map(int, input().split()))

r = 0
c = 0
for i in s:
    if i == -1:
        if r > 0:
            r -= 1
        else:
            c += 1
    else:
        r += i
print(c)
