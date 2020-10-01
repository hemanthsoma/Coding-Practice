a,b =list(map(int,input().split()))
l=[] 
for i in range(a):
    l.append(list(map(int,input().split())))
s=0
for j in range(b):
    for i in range(a):
        s = s + l[i][j]
    print(s,end=' ')
    s=0
