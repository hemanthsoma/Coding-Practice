n=int(input())
for i in range(n,0,-1):
    c=1;d=i
    for j in range(i):
        if n%2==0:
            if i%2==0:
                print(c,end='')
                c+=1
            elif i%2!=0:
                print(d,end='')
                d-=1
        elif n%2!=0:
            if i%2!=0:
                print(c,end='')
                c+=1
            elif i%2==0:
                print(d,end='')
                d-=1         
    print()