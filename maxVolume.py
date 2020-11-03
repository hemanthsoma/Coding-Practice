n=int(input())
l=list(map(int,input().split()))
i,h=map(int,input().split())
s=i 
for j in range(n):
    s+=l[j]
    if s>h:
        s=l[j]
    if s==h:
        break
if s==h:
    print(1)
else:
    print(-1)