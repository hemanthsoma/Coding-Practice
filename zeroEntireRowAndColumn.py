'''
Given 2 numbers N and M followed by a matrix of size N * M.if there is any entry which is 0 change the entire column and row to zero respectively and then print the matrix.
Input Size : 1 <= N <= 1000
Sample Testcases :
INPUT
2 3
1 0 1
1 1 1
OUTPUT
0 0 0
1 0 1
'''
n,m=map(int,input().split())
l=[];r=[];c=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            r.append(i);c.append(j)
for i in range(n):
    for j in range(m):
        if i in r or j in c:
            print(0,end=' ')
        else:
            print(l[i][j],end=' ')
    print()
