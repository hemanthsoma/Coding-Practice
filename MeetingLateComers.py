l=list(map(str,input().split()))
c=0;d=0
for i in l:
    for j in range(len(i)):
        y = i.index(':')
    if int(i[0:y])==10 and int(i[y+2:])>0:
        c+=1
    if int(i[0:y])>10 and int(i[y+2:])>=0:
        d+=1
print(c+d)
