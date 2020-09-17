l=list(map(int,input().split()))
for i in range(len(l)):
    mi=i
    for j in range(i+1,len(l)):
        if l[j]<l[mi]:
            mi=j 
    l[mi],l[i]=l[i],l[mi]
print(*l)
