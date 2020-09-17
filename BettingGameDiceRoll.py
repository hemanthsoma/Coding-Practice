l=list(map(int,input().split()))
a=int(input())
b=int(input())
m=len(l)
s=[];t=[];c=0;d=0
for i in l:
    if i%2==0:
        s.append(i)
    else:
        t.append(i)
for i in s:
    c+=1
for i in t:
    d+=1
a=a*d
b=b*c  
print(a-b)
