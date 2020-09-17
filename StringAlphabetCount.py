n=input()
l=[]
m=sorted(set(n))
for j in m:
    l.append(j+str(n.count(j)))
print(*l,end=' ')
