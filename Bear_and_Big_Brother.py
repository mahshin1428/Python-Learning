a,b = map(int,input().split())

year = 1
for i in range(1,10):
    if a*3 > b*2 :
       print(year)
       break
    else:
        a=a*3
        b=b*2
        year +=1


