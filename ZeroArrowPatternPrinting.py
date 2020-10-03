n=int(input())
r=(2*n)-1
for i in range(r):
    for j in range(n):
        if j==n-1 or i+j==r//2 or i-j==r//2:
            print(0,end=' ')
        else:
            print('*',end=' ')
    print()
'''
input
5

output 
* * * * 0 
* * * 0 0 
* * 0 * 0 
* 0 * * 0 
0 * * * 0 
* 0 * * 0 
* * 0 * 0 
* * * 0 0 
* * * * 0 
'''
