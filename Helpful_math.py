s = input("")
x = s.split("+")
print(x)
x.sort()
num = "+".join(map(str, x))

print(num)
