from itertools import combinations
n=list(map(str,input().strip()))
c=int(input())
l=[]
for i in combinations(n,c):
    l.append(i)
l=sorted(set(l))
for i in l:
    print(*i,sep='')
