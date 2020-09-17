l=list(map(str,input().split()))
c=int(input())
x=0
d=[]
for i in l:
    if l.count(i) == c:
        d.append(i)
z=set(d)
for i in z:
    x+=1
print(x)
