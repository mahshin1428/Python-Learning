s1 = input('')
s2 = input('')

out = ''
for i in range(len(s1)):
    if s1[i] == s2[i]:
        out = out + '0'

    else:
        out = out + '1'
print(out)
