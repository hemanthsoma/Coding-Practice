'''
Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
Sample Testcase :
INPUT
R P
OUTPUT
P
'''
n,m=input().split()
if n=='R' and m=='R' or m=='P' or n=='P':
    print('D')
elif n=='R':print('P')
else:print('R')
