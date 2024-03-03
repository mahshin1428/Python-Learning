def max_increasing_subarray_length(n, arr):
    max_length = 1
    current_length = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


n = int(input())
arr = list(map(int, input().split()))

print(max_increasing_subarray_length(n, arr))
