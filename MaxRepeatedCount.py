l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i):
        r.append(l.count(i))
t=max(r)
for i in l:
    if l.count(i) == t:
        print(i)
        break 
