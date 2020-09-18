a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    o=0
    for j in range(i,len(l)):
        if(l[j]%2):
            o+=1
        if(o==b):
            c+=1
print(c)
