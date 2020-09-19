a,b=list(map(int,input().split()))
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
p=[[] for i in range(b)]
for i in range(a):
    k=0
    for j in range(k,b):
        if j == k:
            p[k].append(l[i][j])
        k+=1
y=[]
for i in p:
    y.append(sorted(i))
t=zip(*y)
for i in t:
    print(*i,sep=' ')
