'''
The program must accept two integers N and X as the input. The program must print the number of subsets of N divisible
by X as the output.
Boundary Condition(s):
1 <= N, X <= 10^18
Input Format:
The first line contains N and X separated by space.
Output Format:
The first line contains the number of subsets of N divisible by X.
Example Input/Output 1:
Input:
1219945 11
Output:
4
Explanation:
The four subsets of 1219945 divisible by 11 are given below.
121, 99, 12199 and 219945.
Example Input/Output 2:
Input:
999 3
Output:
6
Explanation:
The six subsets of 999 divisible by 3 are given below.
9, 9, 9, 99, 99 and 999.
Example Input/Output 3:
Input:
100452 257
Output:
0
'''
n,m=input().split()
m=int(m);c=0
for i in range(len(n)):
    s=''
    for j in range(i,len(n)):
        s+=n[j]
        if int(s)%m==0:
            if int(s)==0:
                continue
            else:
                c+=1
print(c)
