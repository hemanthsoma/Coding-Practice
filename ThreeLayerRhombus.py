n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1 or i+j==n+3 or i+j==n+5:
            print("/",end='')
        else:
            print("#",end='')
    for j in range(1,n+1):
        if i-j==0 or i-j==2 or i-j==4:
            print("\\",end='') 
        else:
            print("#",end='')
    print()     
for i in range(1,n+1):
    for j in range(1,n+1):
        if i-j==0 or j-i==2 or j-i==4:
            print("\\",end='') 
        else:
            print("#",end='')
    for j in range(1,n+1):
        if i+j==n+1 or i+j==n-1 or i+j==n-3:
            print("/",end='') 
        else:
            print("#",end='')
    print()  
