n=int(input())
n=n+1
for i in range(n):
    c=1;k=[]
    for j in range(i+1):
        if i==0 or j==0:
            print('*',end='')
        else:
            print(c,end='')
            k.append(c)
            c+=1
    print(*k[::-1][1:],end='',sep='')
    if i!=0:
        print('*',end='')
    print()
for i in range(n-1,1,-1):
    c=1;k=[]
    for j in range(i):
        if i==0 or j==0:
            print('*',end='')
        else:
            print(c,end='')
            k.append(c)
            c+=1
    print(*k[::-1][1:],end='',sep='')
    if i!=0:
        print('*',end='')
    print()
print('*')
