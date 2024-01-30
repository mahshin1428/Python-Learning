nk_input = input()
n, k = map(int, nk_input.split())


scores_input = input()
scores = list(map(int, scores_input.split()))

next_round = 0
for i in range(n):
    if scores[i] > 0 and scores[i] >= scores[k-1]:
        next_round += 1

print(next_round)
