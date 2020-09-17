n=int(input())
l=list(map(int,input().split()))
m=[i for i in l]
for i in range(len(l)):
    if i==0:
        m[i]=l[i]+abs(l[i+1])
    elif i==len(l)-1:
        m[i]=l[i]+abs(l[i-1])
    else:
        m[i]=l[i]+abs(l[i+1]-l[i-1])
print(*m,end=' ')
