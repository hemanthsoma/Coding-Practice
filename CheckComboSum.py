from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for j in range(1,n+1):
    for i in combinations(l,j):
        t=sum(i)
        if t==m:
            c+=1
print(c)
