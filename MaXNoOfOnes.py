n,m=map(int,input().split())
l=[];t=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in l:
    for j in i:
        if j==1:
            t.append(i.count(j))
print(max(t))