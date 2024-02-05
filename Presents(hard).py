n = int(input())
gift_givers = list(map(int, input().split()))

gift_receivers = [0] * n

for i in range(n):
    gift_receivers[gift_givers[i] - 1] = i + 1

print(*gift_receivers)
