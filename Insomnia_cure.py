k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damaged_dragons = 0

for dragon in range(1, d + 1):
    if dragon % k == 0 or dragon % l == 0 or dragon % m == 0 or dragon % n == 0:
        damaged_dragons += 1

print(damaged_dragons)
