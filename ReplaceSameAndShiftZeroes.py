l=list(map(int,input().split()))
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        l[i] = l[i]*2
        l[i+1] = 0
print(*([i for i in l if i!=0]+[0 for _ in range(l.count(0))]))
