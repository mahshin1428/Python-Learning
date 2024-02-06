n, m = map(int, input().split())

snake = []

for i in range(0, n):
    if i % 4 == 1:
        snake.append("." * (m - 1) + "#")
    elif i % 4 == 3:
        snake.append("#" + "." * (m - 1))
    else:
        snake.append("#" * m)

for row in snake:
    print(row)
