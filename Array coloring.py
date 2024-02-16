def can_color_array(num, a):
    sum_odd = sum_even = 0
    for i in range(num):
        if i % 2 == 0:
            sum_even += a[i]
        else:
            sum_odd += a[i]
    if (sum_even % 2 == 0 and sum_odd % 2 == 0) or (sum_even % 2 != 0 and sum_odd % 2 != 0):
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_color_array(n, arr))
