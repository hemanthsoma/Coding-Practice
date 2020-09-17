a,b,c,d=list(map(int,input().split()))
e=0
if c%2==0:
    e=c//2
else:
    e=(c+1)//2
while c<=d:
    if c%2!=0:
        print(a*e,end=' ')
    else:
        print(b*e,end=' ')
        e+=1
    c+=1
