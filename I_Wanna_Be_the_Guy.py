n = int(input())

a1 = set(map(int, input().split()))
a2 = set(map(int, input().split()))

s = {1, 2, 3, 4}
s3 = a1 | a2

if len(s3) == n and s3 == s:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
