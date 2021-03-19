'''
The program must accept the names of the colors in an LED serial set as the input. The program must find the number of
groups of LEDs having the same color at the beginning and the end in the given LED serial set. Also consider each LED in
the given LED serial set as a group. Finally, the program must print the number of groups of LEDs as the output.
Boundary Condition(s):
1 <= Length of each color's name <= 20
Input Format:
The first line contains a space separated string values representing the names of the colors in an LED serial set.
Output Format:
The first line contains the number of groups LEDs having the same color at the beginning and the end in the given LED
serial set.
Example Input/Output 1:
Input:
Red Blue Green Blue
Output:
5
Explanation:
The 5 groups of LEDs are given below.
Red
Blue
Green
Blue
Blue Green Blue
Example Input/Output 2:
Input:
Yellow Red Yellow Green Blue Yellow Green
Output:
11
Explanation:
The 11 groups of LEDs are given below.
Yellow
Red
Yellow
Green
Blue
Yellow
Green
Yellow Red Yellow
Yellow Red Yellow Green Blue Yellow
Yellow Green Blue Yellow
Green Blue Yellow Green
'''
s=input().split()
c=len(s)
for i in range(len(s)):
    d=''
    for j in range(i,len(s)):
        d+=s[j]
        if d[:len(s[i])]==d[-len(s[i]):] and d.count(s[i])>1:
            c+=1
print(c)
