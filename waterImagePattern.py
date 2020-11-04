n,m=map(int,input().split())
for i in range(m):
    for j in range(i+1):
        print(n,end='')
    print()
    n+=1
for i in range(m,0,-1):
    for j in range(i):
        print(n-1,end='')
    print()
    n-=1