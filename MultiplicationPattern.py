'''
The program must accept an integer N as the input. The program must print the desired pattern as shown in the
Example Input/Output Sections.
Boundary Condition(s):
1 <= N <= 100
Example Input/Output 1:
Input:
5
Output:
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
Example Input/Output 2:
Input:
6
Output:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''
n=int(input())
p=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j*p,end=' ')
    print()
    p+=1
