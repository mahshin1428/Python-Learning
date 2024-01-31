n = int (input())

s = input("")
num = 0
if len(s) == n and s.isupper():
   for i in range(1,n):
       if s[i] == s[i-1]:
           num +=1


print(num)
