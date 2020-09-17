n=input()
l=[];t=[]
for i in n:
    if i.isupper():
        l.append(i)
    else:
        t.append(i)
l,t=sorted(l),sorted(t)
if len(l)<len(t):
    f,s=t[:len(l)],t[len(l):]
else:
    f,s=l[:len(t)],l[len(t):]
p,q=[],[]
for i in zip(l,t):
    q.append(list(i))
for i in q:
    for j in i:
        p.append(j)
print(*(p+s),sep='')
