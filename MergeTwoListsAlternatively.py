l=list(map(int,input().split()))
m=list(map(str,input().split()))
ll,ml=len(l),len(m)
if ll<ml:
    f,s=m[:ll],m[ll:]
else:
    f,s=l[:ml],l[ml:]
t,r=[],[]
for i in zip(l,m):
    r.append(list(i))
for i in r:
    for j in i:
        t.append(j) 
print(*(t+s),end=" ")
