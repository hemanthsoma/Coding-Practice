'''
The program must accept a string S as the input. The program must print only the most repeated characters in the string S as the output. If more than one character is repeated maximum number of times, then the characters must be printed in the order of their occurrence as the output. If there are no repeated characters in S, then the

program must print S as the output.

Boundary Condition(s):

1 <= Length of S <= 100

Input Format:

The first line contains the value of S.

Output Format:

The first line contains the most repeated character in the order of their occurrences.

Example Input/Output 1:

Input

apple

Output:

PP

Explanation:

The most repeated character is p which is occurred two times in apple.

Hence the output is pp

Example Input/Output 2:

Input:

#XRREETRE

Output:

RREERE
'''
from collections import Counter
k=input()
n=[i for i in k]
c=Counter(n)
m=max(n.count(i) for i in n)
s=''
for i in c:
    if c[i]==m:
        s+=i
for i in n:
    if i in s:
        print(i,end='')
