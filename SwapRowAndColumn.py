a = int(input())
l=[] 
for i in range(a):
    l.append(list(map(int,input().split())))
for i in range(a):
    for j in range(0,a):
        if i==0:
            l[0][j],l[a-1][j] = l[a-1][j],l[0][j]
for i in range(a):
    for j in range(a):
        print(l[i][j],end=' ')
    print()
