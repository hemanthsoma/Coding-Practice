n,m=input().split()
l=[]
n,m=int(n),int(m)
for i in range(n):
    l.append(list(map(int,input().strip().split())))
q=[]
for i in range(n):
    r=[]
    for j in range(m):
        if j==m-1 or j==m-2 and i==1 or i==0:
            t=sum(map(int,str(l[i][j])))
            if l[i][j]%t==0:
                q.append(l[i][j])
    r.append(q)
print(q) 
