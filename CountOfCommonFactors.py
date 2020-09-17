n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=max(l)
r=0
for i in range(2,m+1):
    c=0
    for j in range(0,len(l)):
        if l[j]%i==0:
            c+=1
    if c==len(l):
        r+=1
print(r)
