a, b = map(int, input().split())
y = 0
x = min(a, b)
if abs(a-b)//2 != 0:
    y = abs(a-b)//2

print(x, y)
