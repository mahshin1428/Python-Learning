t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if len(set(arr)) < len(arr):
        print("NO")
    else:
        arr.sort()
        if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
            print("YES")
        else:
            print("NO")
