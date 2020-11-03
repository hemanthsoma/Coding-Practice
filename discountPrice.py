n=int(input())
l=[];t=[]
for i in range(n):
    l.append(int(input()))
c=1
t.append(l[0])
for i in range(1,n):
    p = l[i] 
    d = min(l[:c+1])
    if p>d:
        t.append(p-d)
    c+=1
print(sum(t))