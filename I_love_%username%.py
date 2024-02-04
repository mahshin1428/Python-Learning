n = int(input())

p = list(map(int, input().split()))
count = 0
high = low = p[0]
for i in range(n):
    if p[i] > high or p[i] < low:
        count += 1

    high = max(high, p[i])
    low = min(low, p[i])

print(count)
