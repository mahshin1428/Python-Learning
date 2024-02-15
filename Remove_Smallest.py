t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    flag = False
    for i in range(len(a)):
        if a[i] - a[i - 1] > 1:
            flag = True
            print('NO')
            break
    if flag is False:
        print("yes")
