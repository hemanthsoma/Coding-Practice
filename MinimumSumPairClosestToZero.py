from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
t=[];p=[]
for i in range(1,n+1):
    for j in combinations(l,i):
        if sum(list(j))<0:
            t.append(list(j))
        elif sum(list(j))==0:
            p.append(list(j))
m=sum(t[0]);k=[]
for i in t:
    if sum(i)>m:
        m=sum(i)
        k=i
print(*k) if k!=[] else print(*p[0])