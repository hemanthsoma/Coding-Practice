n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l),2):
    if l[i]==1 and l[i-1]==0:
        l[i-1]=1
    elif l[i]==0 and l[i-1]==1:
        l[i]=1
    elif l[i-1]==0 and l[i-1]==0:
        l[i-1]=1
print(l)
