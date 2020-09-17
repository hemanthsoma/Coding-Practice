n=list(map(str,input().split(',')))
l=[]
for i in n:
    t=[]
    f=i.index(':')
    k=i[f+1:]
    for j in k:
        p=(int(j)**2)
        t.append(p)
    l.extend([i[:f],sum(t)])
for i in range(1,len(l),2):
    if l[i]%2!=0:
        print(l[i-1][2:]+l[i-1][:2])
    else:
        print(l[i-1][-1]+l[i-1][:-1])
