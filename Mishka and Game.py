n = int(input())

mis = 0
cri = 0
for _ in range(n):
    mi, ci = map(int, input().split())
    if mi > ci:
        mis += 1
    else:
        cri += 1

if mis > cri:
    print("Mishka")
elif mis < cri:
    print("Chris")
else:
    print("Friendship is magic!^^")
