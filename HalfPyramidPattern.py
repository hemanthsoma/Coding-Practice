n=int(input())
n=n-1
for i in range(-1,n):
    for j in range(i+1):
        print('b',end='')
    for j in range(n-i-1):
        print('*',end='')
    for j in range(n-1,i-1,-1):
        print('*',end='')
    for j in range(i+1):
        print('b',end='')
    print()

'''
Input 
5 
Output
*********
b*******b
bb*****bb
bbb***bbb
bbbb*bbbb
'''
