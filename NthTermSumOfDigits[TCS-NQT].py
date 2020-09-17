n=int(input())
l=[0]*(n+6)
f=0;p=1
for i in range(5):
    f=f+p
    l.insert(i,f) 
    p=f
    f=p
l.insert(0,1)
s=0
for i in range(5):
    s+=l[i]
for i in range(6,n):
    while l[i-1]>0:
        s+=l[i-1]%10
        l[i-1]//=10
    l[i]=s 
print(l[n-1])
