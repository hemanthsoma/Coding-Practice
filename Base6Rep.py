r=''
n=int(input())
val = list(map(int,input().split(',')))
i=0
m=[]
while(i<len(val)):
    while(val[i]>0):
        r=str(val[i]%6)+r
        val[i]//=6
    m.append(r)
    i+=1
print(*m)
