l=list(map(int,input().split()))
l=sorted(l)
r=0
for i in range(4):
    f=l[i]+l[i+1]
    if f in l:
        s=l.index(l[i+1])
        r=l.index(f)
        l.insert(s+1,l[r])
    l[i+1]=f
    f=l[i]
print(*l)
