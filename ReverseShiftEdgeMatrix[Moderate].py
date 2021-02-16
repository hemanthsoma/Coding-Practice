a,b=map(int,input().split())
l=[]
for _ in range(a):
    l.append(input().split())
for i in range(a):
    for j in range(b):
        if i==0 and j==0:
            print(int(l[1][0][::-1]),end=' ')
        elif i==0 and j!=0:
            print(int(l[i][j-1][::-1]),end=' ')
        elif i==a-1 and j==b-1:
            print(int(l[a-2][b-1][::-1]),end=' ')
        elif i==a-1:
            print(int(l[i][j+1][::-1]),end=' ')
        elif j==0:
            if i!=0 and i!=a-1:
                print(int(l[i+1][j][::-1]),end=' ')
        elif j==b-1:
            if i!=0 and i!=a-1:
                print(int(l[i-1][j][::-1]),end=' ')
        else:
            print(l[i][j],end=' ')
    print()
    
'''
Input:
4 4
85 84 12 26
33 43 91 95
98 17 45 66
57 17 73 10
Output:
33 58 48 21 
89 43 91 62 
75 17 45 59 
71 37 1 66 
'''
