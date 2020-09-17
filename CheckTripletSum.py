from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in combinations(l,3):
    t=list(i)
    if sum(t)==m:
        c+=1
print(c)
