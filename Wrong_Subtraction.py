n, k = map(int, input().split())
val = 0
for i in range(k):
    if n % 10 == 0:
        n = n // 10
        k -= 1
    else:
        n = n - 1
        k -= 1

print(n)
