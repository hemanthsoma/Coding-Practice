from string import ascii_uppercase
l=[i for i in ascii_uppercase]*2
n,m=map(int,input().split())
for i in range(m):
    for j in range(i+1):
        print(l[n-1],end=' ')
        n=n+1
    print()
    n=n-i-1
'''
25 4
Y 
Y Z 
Y Z A 
Y Z A B
'''
