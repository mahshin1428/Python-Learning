n = int(input())

count = 1
m = [input() for _ in range(n)]
count = 1

for i in range(1, n):
    if m[i] != m[i-1]:
        count += 1


print(count)
