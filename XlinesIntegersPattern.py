'''
The program must accept two integers N and X as the input. The program must print the desired pattern as shown in
the Example Input/Output section.
Boundary Condition(s):
1 <= N <= 100
1 <= X <= 10
Example Input/Output 1:
Input:
8 5
Output:
8
16 17
24 25 26 27
32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55
Example Input/Output 2:
Input:
9 4
Output:
9
18 19
27 28 29 30
36 37 38 39 40 41 42 43
'''
n,m=map(int,input().split())
p=1
for i in range(1,m+1):
    c=0
    for j in range(1,p+1):
        j=(n*i)
        print(j+c,end=' ')
        c+=1
    print()
    p=p*2
