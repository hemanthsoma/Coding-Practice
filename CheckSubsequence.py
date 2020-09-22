'''
The program must accept two string values S1 and S2 as the input. The program must print Found if S2 is a
subsequence of S1. Else the program must print NotFound as the output. The string S2 is said to be a subsequence of
string S1 if all the characters of S2 are present in S1 in the same order.
Boundary Condition(s):
1 <= Length of S1, S2 <= 10^5
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains Found or NotFound based on the given condition.
Example Input/Output 1:
Input:
management
amet
Output:
Found
Explanation:
The subsequence amet is present in management so Found is printed.
Example Input/Output 2:
Input:
telescope
lspc
Output:
NotFound

'''
n=input()
m=input()
i = iter(n)
if (all(any(c==ch for c in i) for ch in m)):
    print("Found")
else:
    print("NotFound")
