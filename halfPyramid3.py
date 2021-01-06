n=int(input())
for i in range(n):
    c=1;d=2
    for j in range(i+1):
        if i%2!=0:
            print(d,end='')
            d+=2
        elif i%2==0:
            print(c,end='')
            c+=2
    print()