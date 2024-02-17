s = input()
x = set(s.replace("{", "").replace("}", "").replace(",", "").replace(" ", ""))

a = len(x)
print(a)
