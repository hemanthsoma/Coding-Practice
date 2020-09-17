a,b=list(map(int,input().split()))
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
new = [[] for i in range(a+b-1)]
for i in range(a):
    for j in range(b):
        s=i+j 
        if(s%2==0):
            new[s].insert(0,l[i][j])
        else:
            new[s].append(l[i][j])
if (a+b)%2==0:
    for i in new[::-1]:
        print(*i,end=' ')
else:
    for i in new[::-1]:
        print(*i[::-1],end=' ')
