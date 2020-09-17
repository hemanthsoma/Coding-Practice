s=input().lower().split()
l=[]
for i in s:
    for j in range(0,len(i)):
        if j%2==0:
            l.append(i[j].upper())
        else:
            l.append(i[j].lower())
    l.append(' ')
print(*l,sep='')
