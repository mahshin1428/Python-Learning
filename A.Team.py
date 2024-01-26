def problem(times, number):
    count = 0

    for start in range(n):
        sure_count = number[start].count(1)

        if sure_count >= 2:
            count += 1
    return count


n = int(input())

num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

result = problem(n, num)
print(result)
