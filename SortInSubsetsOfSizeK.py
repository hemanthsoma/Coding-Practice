a,b=input().split()
l=list(map(int,input().split()))
a,b=int(a),int(b)
p=[]
i=0;k=b
while(i<len(l)):
    p.extend([l[i:k]])
    i+=b
    k+=b
for i in p:
    print(*sorted(i),end=' ')
