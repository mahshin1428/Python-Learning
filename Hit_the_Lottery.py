n = int(input())

coins = [100, 20, 10, 5, 1]
num_coin = 0
for i in coins:
    count = n // i
    num_coin += count
    n -= count*i

    if n == 0:
        break

print(num_coin)

