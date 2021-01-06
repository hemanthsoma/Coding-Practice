n=int(input());d=n
for i in range(n):
    c=1
    for j in range(n):
        if i==0:
            print(c,end='')
            c+=1
        elif j==0:
            print(1,end='')
        elif i+j==n-1:
            print(d,end='')
        else:
            print(' ',end='')
    print()
    d-=1
'''
5
12345
1  4 
1 3  
12   
1
'''