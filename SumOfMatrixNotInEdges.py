n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().rstrip().split())))
s=[]
for i in range(n):
    for j in range(n):
        if i!=0 and j!=0 and i!=n-1 and j!=n-1:
            s.append(mat[i][j])
print(sum(s))
