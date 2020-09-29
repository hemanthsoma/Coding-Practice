n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if i>0:
        if i%2==0:
            s+=int(str(i)[::-1])
        else:
            s+=i
print(s)
