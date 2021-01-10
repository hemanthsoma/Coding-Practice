def pattern(n,m):
    for i in range(n):
        for j in range(m):
            if i==0 or i==n//2 or i==n-1:
                if j==0 or j==n//2 or j==m-1:
                    print('+',end=' ')
                else:
                    print('-',end=' ')
            elif j==0 or j==n//2 or j==m-1:
                print('|',end=' ')       
            else:
                print(' ',end=' ')
        print()
n=11;m=10
pattern(n,m)
'''
+ - - - - + - - - + 
|         |       | 
|         |       | 
|         |       | 
|         |       | 
+ - - - - + - - - + 
|         |       | 
|         |       | 
|         |       | 
|         |       | 
+ - - - - + - - - + 
'''
