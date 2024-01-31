n = int(input())

s = (input("").upper())
an = s.count('A')
da = s.count('D')
if an > da:
    print("Anton")
if an < da:
    print("Danik")
if an == da:
    print("Friendship")
