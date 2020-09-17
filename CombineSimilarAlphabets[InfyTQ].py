n=input()
k=sorted(set(n.upper()))
l=[]
for i in range(len(k)):
    t=""
    for j in n:
        if k[i]==j.upper():
            t+=j 
    l.append(t)
i,j=0,len(l)-1
res=""
while(i<=j):
    if i==j:
        res+=l[i]
    else:
        res+=l[i]+l[j]
    i+=1
    j-=1
print(res)
