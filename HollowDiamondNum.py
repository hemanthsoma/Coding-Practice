n=int(input())
t=(n*2)-1
r=(n**2)-(n-2)**2
l=[i for i in range(1,r+1)]
y=l[t:][::-1];u=y
for i in range(t):
    for j in range(t):
        if i+j==n-1 or i-j==n-1:
            print(l[i],end=' ')
        elif i!=0 and j-i==n-1:
            print(y[i-1],end=' ')
        elif i!=t-1 and i+j==t+1+(n-3):
            print(u[i-1],end=' ')
        else:
            print(0,end=' ')
    print()
'''
6
0 0 0 0 0 1 0 0 0 0 0 
0 0 0 0 2 0 20 0 0 0 0 
0 0 0 3 0 0 0 19 0 0 0 
0 0 4 0 0 0 0 0 18 0 0 
0 5 0 0 0 0 0 0 0 17 0 
6 0 0 0 0 0 0 0 0 0 16 
0 7 0 0 0 0 0 0 0 15 0 
0 0 8 0 0 0 0 0 14 0 0 
0 0 0 9 0 0 0 13 0 0 0 
0 0 0 0 10 0 12 0 0 0 0 
0 0 0 0 0 11 0 0 0 0 0 
'''