n=''.join(input().split())
l=[];c=0
for i in n:
    if i in '1234567890':
        l.append(int(i))
    elif i in 'abcdefghijklmnopqrstuvwxyz':
        continue
    else:
        c+=1
if c%2!=0:
    t=[];p=[]
    for i in l:
        if i%2!=0:
            t.append(i)
        else:
            p.append(i)
    if len(t)<len(p):
        f,s=p[:len(t)],p[len(t):]
    else:
        f,s=t[:len(p)],t[len(p):]
    x,y=[],[]
    for i in zip(t,p):
        y.append(list(i))
    for i in y:
        for j in i:
            x.append(j)
    print(*(x+s),sep=' ')
else:
    t=[];p=[]
    for i in l:
        if i%2==0:
            t.append(i)
        else:
            p.append(i)
    if len(t)<len(p):
        f,s=p[:len(t)],p[len(t):]
    else:
        f,s=t[:len(p)],t[len(p):]
    x,y=[],[]
    for i in zip(t,p):
        y.append(list(i))
    for i in y:
        for j in i:
            x.append(j)
    print(*(x+s),sep=' ')
