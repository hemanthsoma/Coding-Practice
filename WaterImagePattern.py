n,m=map(int,input().split())
for i in range(m):
    for j in range(i+1):
        print(n,end='')
    print()
    n+=1
for i in range(m,0,-1):
    for j in range(i):
        print(n-1,end='')
    print()
    n-=1

'''
Input 
2 5

Output 
2
33
444
5555
66666
66666
5555
444
33
2
'''
