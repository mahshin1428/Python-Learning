n = int(input())

h = 0
c = 0

while c <= n:
    h += 1
    c += h * (h+1)//2
print(h-1)




