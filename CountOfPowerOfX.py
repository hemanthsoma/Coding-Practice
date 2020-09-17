a,b=input().split()
l=list(map(int,input().split()))
a,b=int(a),int(b)
m=[]
for i in l:
    r=[]
    for k in range(1,i+1):
        if i%k==0:
            r.append(k)
    m.append(r)
c=0;d=0
for i in m:
    for j in range(1,len(i)):
        if i[j]%b!=0:
            c+=1
        d+=1
print(d)
