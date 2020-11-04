n=int(input())
l=[];t=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in l:
    t.append(i[::-1])
m=zip(*t)
for i in m:
    print(*i)
'''
Input

3
45 10 98
75 58 85
94 44 91
Output

98 85 91
10 58 44
45 75 94
