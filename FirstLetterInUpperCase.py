n=input()#she is    happy
m=list(str(n[0].upper())+n[1::])
l=[]
for i in range(len(m)):
    if m[i]==' ' and m[i+1]==str(m[i+1]):
        m[i+1]=m[i+1].upper()
print(*m,sep='')
