n = int(input())
cap = 0
ma = 0
for _ in range(n):
    a, b = map(int, input().split())
    cap = cap - a + b
    if cap > ma:
        ma = cap

print(ma)
