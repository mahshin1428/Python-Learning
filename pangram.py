n = int(input())
s = str(input()).lower()

x = set(s)

if set('abcdefghijklmnopqrstuvwxyz').issubset(x):
    print("YES")

else:
    print("NO")
