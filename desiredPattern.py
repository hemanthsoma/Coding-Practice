n=int(input())
for i in range(n):
    for j in range(1,n+1):
        if i+j==n:
            print(j,end='')
        elif j==1:
            print(j,end='')
        elif i==0:
            print(j,end='')
        else:
            print(' ',end='')
    print()

'''
5
12345
1  4 
1 3  
12   
1  
'''
