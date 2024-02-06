n = int(input())

total = 0
if n % 2 == 0:
    total = n // 2
else:
    total = (n - 1) // 2 - n
print(total)
