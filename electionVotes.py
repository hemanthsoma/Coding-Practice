n=int(input())
l=[]
for i in range(n):
    l.append(input())
t=[]
for i in l:
    if l.count(i)>=2:
        t.append(i)
print(*sorted(t)[-1],end='',sep='')