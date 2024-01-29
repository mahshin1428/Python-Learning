r=5
c=5
m=[]


for i in range(r):
    row_val = list(map(int,input().split()))
   # print( row_val)
    m.append(row_val)

for i in range(r):
    for j in range(c):
        if m[i][j]==1 :
         row_one, col_one = i, j


moves = abs(row_one - 2) + abs(col_one - 2)

print(moves)
