s1 = input('')
s2 = input('')

if s1.lower() == s2.lower():
    print("0")
for i in range(len(s2)):
    if ord(s1[i].lower()) > ord(s2[i].lower()):
        print("1")
        break
    if ord(s1[i].lower()) < ord(s2[i].lower()):
        print("-1")
        break

