'''
Write a code to generate a square pattern using numbers.

Input Description:
Given an integer R indicates number of R*2-1 rows.

Where 1<=R<=100.

Output Description:
Print the square pyramid number based on the given integer R.

Sample Input :
5
Sample Output :
1
1 4
1 4 9
1 4 9 16
1 4 9 16 25
1 4 9 16
1 4 9
1 4
1
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*j,end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j*j,end=' ')
    print()
