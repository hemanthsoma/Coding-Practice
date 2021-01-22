'''
Given a string S and an occurrence frequency N, find the last character in the String that appears exactly N times. If there is no such character occurring N times, print -1 as the output.
Boundary Condition(s):
2 <= Length of S <= 10^6
Input Format:
The first line contains the string S.
The second line contains the integer
Output Format:
N.
The first line contains either the last character in the String that appears exactly N times or -1.
Example Input/Output 1:
Input:
skillrack
2
Output
k
Explanation:
Characters occurring 2 times are kl.
The last occurring character is k and hence it is printed as the output.
Example Input/Output 2:
Input
-!!-==!-
3
Output:
-
'''
from collections import Counter
n=[i for i in input().strip()]
m=int(input())
c=Counter(n)
t=''
for i in n[::-1]:
    if n.count(i)==m:
        t=i
        break
for i in c:
    if c[i]==m and i==t:
        print(i)
        exit()
else:
    print(-1)
