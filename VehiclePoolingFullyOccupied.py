from itertools import combinations
a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
c=0
for i in range(1,b+1):
    for j in combinations(l,i):
        if sum(j)==a:
            c+=1
print(c)
