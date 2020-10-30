def Xpattern(i):
    for j in range(1,n):
        if i==j:
            print(j,end='')
        else:
            print(' ',end='')
    for j in range(n,0,-1):
        if i==j:
            print(j,end='')
        else:
            print(' ',end='')
    print()
n=int(input())
for i in range(1,n+1):
    Xpattern(i)
for i in range(n-1,0,-1):
    Xpattern(i)
