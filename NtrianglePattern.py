m=int(input());n=1
while(n<=m):
    for i in range(n):
        for j in range(i+1,0,-1):
            print(j,end=' ')
            j+=1
        print() 
    for i in range(n-1,0,-1):
        for j in range(i):
            print(i,end=' ')
            i-=1
        print()
    n+=1
'''
Input
4
Output
1 
1 
2 1 
1 
1 
2 1 
3 2 1 
2 1 
1 
1 
2 1 
3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''
